import streamlit as st
from auth.auth_utils import init_db
from components.login_page import show_login_page

st.set_page_config(page_title="TalkHeal", page_icon="💬", layout="wide")

# --- DB Initialization ---
if "db_initialized" not in st.session_state:
    init_db()
    st.session_state["db_initialized"] = True

# --- Auth State Initialization ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

# --- LOGIN PAGE ---
if not st.session_state.authenticated:
    show_login_page()
    st.stop()

# --- TOP RIGHT BUTTONS: THEME TOGGLE & LOGOUT ---
if st.session_state.get("authenticated", False):
    col_spacer, col_theme, col_logout = st.columns([5, 0.5, 0.7])
    with col_spacer:
        pass  # empty spacer to push buttons right
    with col_theme:
        is_dark = st.session_state.get('dark_mode', False)
        if st.button("🌙" if is_dark else "☀️", key="top_theme_toggle", help="Toggle Light/Dark Mode", use_container_width=True):
            st.session_state.dark_mode = not is_dark
            st.session_state.theme_changed = True
            st.rerun()
    with col_logout:
        if st.button("Logout", key="logout_btn", use_container_width=True):
            for key in ["authenticated", "user_email", "user_name", "show_signup"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

# --- MAIN UI (only after login) ---
header_col1, header_col2, header_col3 = st.columns([6, 1, 1])
with header_col1:
    st.title(f"Welcome to TalkHeal, {st.session_state.user_name}! 💬")
    st.markdown("Navigate to other pages from the sidebar.")

import google.generativeai as genai
from core.utils import save_conversations, load_conversations
from core.config import configure_gemini, PAGE_CONFIG
from core.utils import get_current_time, create_new_conversation
from css.styles import apply_custom_css
from components.header import render_header
from components.sidebar import render_sidebar
from components.chat_interface import render_chat_interface, handle_chat_input

from components.mood_dashboard import render_mood_dashboard
# from components.emergency_page import render_emergency_page
from components.focus_session import render_focus_session
# from components.emergency_page import render_emergency_page
from components.mood_dashboard import render_mood_dashboard
from components.focus_session import render_focus_session

from components.emergency_page import render_emergency_page
from components.profile import apply_global_font_size

# --- 1. INITIALIZE SESSION STATE ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "conversations" not in st.session_state:
    st.session_state.conversations = load_conversations()
if "active_conversation" not in st.session_state:
    st.session_state.active_conversation = -1
# if "show_emergency_page" not in st.session_state:
#     st.session_state.show_emergency_page = False
if "show_focus_session" not in st.session_state:
    st.session_state.show_focus_session = False
if "show_mood_dashboard" not in st.session_state:
    st.session_state.show_mood_dashboard = False
if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = "expanded"
if "mental_disorders" not in st.session_state:
    st.session_state.mental_disorders = [
        "Depression & Mood Disorders", "Anxiety & Panic Disorders", "Bipolar Disorder",
        "PTSD & Trauma", "OCD & Related Disorders", "Eating Disorders",
        "Substance Use Disorders", "ADHD & Neurodevelopmental", "Personality Disorders",
        "Sleep Disorders"
    ]
if "selected_tone" not in st.session_state:
    st.session_state.selected_tone = "Compassionate Listener"

# --- 2. SET PAGE CONFIG ---
apply_global_font_size()

# --- 3. APPLY STYLES & CONFIGURATIONS ---
apply_custom_css()
model = configure_gemini()

# --- 4. TONE SELECTION DROPDOWN IN SIDEBAR ---
TONE_OPTIONS = {
    "Compassionate Listener": "You are a compassionate listener — soft, empathetic, patient — like a therapist who listens without judgment.",
    "Motivating Coach": "You are a motivating coach — energetic, encouraging, and action-focused — helping the user push through rough days.",
    "Wise Friend": "You are a wise friend — thoughtful, poetic, and reflective — giving soulful responses and timeless advice.",
    "Neutral Therapist": "You are a neutral therapist — balanced, logical, and non-intrusive — asking guiding questions using CBT techniques.",
    "Mindfulness Guide": "You are a mindfulness guide — calm, slow, and grounding — focused on breathing, presence, and awareness."
}

with st.sidebar:
    st.header("🧠 Choose Your AI Tone")
    selected_tone = st.selectbox(
        "Select a personality tone:",
        options=list(TONE_OPTIONS.keys()),
        index=0
    )
    st.session_state.selected_tone = selected_tone

# --- 5. DEFINE FUNCTION TO GET TONE PROMPT ---
def get_tone_prompt():
    return TONE_OPTIONS.get(st.session_state.get("selected_tone", "Compassionate Listener"), TONE_OPTIONS["Compassionate Listener"])

# --- 6. RENDER SIDEBAR ---
render_sidebar()

# --- 7. PAGE ROUTING ---
main_area = st.container()

if not st.session_state.conversations:
    saved_conversations = load_conversations()
    if saved_conversations:
        st.session_state.conversations = saved_conversations
        if st.session_state.active_conversation == -1:
            st.session_state.active_conversation = 0
    else:
        create_new_conversation()
        st.session_state.active_conversation = 0
    st.rerun()

# --- 8. RENDER PAGE ---
# if st.session_state.get("show_emergency_page"):
#     with main_area:
#         render_emergency_page()
# else:
if st.session_state.get("show_emergency_page"):
    with main_area:
        render_emergency_page()
elif st.session_state.get("show_focus_session"):
    with main_area:
        render_focus_session()
elif st.session_state.get("show_mood_dashboard"):
    with main_area:
        render_mood_dashboard()
else:
    with main_area:
        render_header()
        st.markdown(f"""
<div style="text-align: center; margin: 20px 0;">
    <h3>🗣️ Current Chatbot Tone: <strong>{st.session_state['selected_tone']}</strong></h3>
</div>
""", unsafe_allow_html=True)
        
        # --- Mood Slider with Keyboard Navigation ---
        def mood_slider():
            slider_html = """
            <div>
                <label for="mood-slider" class="sr-only">Select your mood</label>
                <input type="range" id="mood-slider" min="1" max="5" value="3" step="1"
                       aria-valuemin="1" aria-valuemax="5" aria-valuenow="3"
                       onkeydown="handleKeydown(event)" onchange="updateSliderValue(this.value)">
                <div id="mood-label">Neutral</div>
                <script>
                    function handleKeydown(event) {
                        const slider = document.getElementById('mood-slider');
                        let value = parseInt(slider.value);
                        if (event.key === 'ArrowLeft' && value > 1) {
                            value--;
                        } else if (event.key === 'ArrowRight' && value < 5) {
                            value++;
                        }
                        slider.value = value;
                        slider.setAttribute('aria-valuenow', value);
                        updateSliderValue(value);
                    }
                    function updateSliderValue(value) {
                        const labels = ['Very Sad', 'Sad', 'Neutral', 'Happy', 'Very Happy'];
                        document.getElementById('mood-label').innerText = labels[value - 1];
                        Streamlit.setComponentValue(value);
                    }
                </script>
                <style>
                    #mood-slider {
                        width: 100%;
                        accent-color: #ff69b4; /* Matches the soft pink/magenta UI */
                    }
                    #mood-label {
                        text-align: center;
                        margin-top: 10px;
                        font-size: 16px;
                        color: #333;
                    }
                    .sr-only {
                        position: absolute;
                        width: 1px;
                        height: 1px;
                        padding: 0;
                        margin: -1px;
                        overflow: hidden;
                        clip: rect(0, 0, 0, 0);
                        border: 0;
                    }
                </style>
            </div>
            """
            mood_value = st.components.v1.html(slider_html, height=100)
            return mood_value

        # --- Mood Slider ---
        st.subheader("😊 Track Your Mood")
        mood_options = ['Very Sad', 'Sad', 'Neutral', 'Happy', 'Very Happy']
        mood = st.slider(
            'Select your mood',
            min_value=1, max_value=5, value=3, step=1
)
        coping_tips = {
    1: "It’s okay to feel this way. Try some deep breathing exercises to find calm.",
    2: "Consider writing down your thoughts in the journal to process your feelings.",
    3: "A short walk or some light stretching might help you feel balanced.",
    4: "Great to hear you’re feeling happy! Share something positive in your journal.",
    5: "You’re shining today! Keep spreading that positivity with a kind act."
}
        st.write(f"Selected mood: {mood_options[mood-1]}")
        st.write(f"Coping tip: {coping_tips.get(mood, 'Let’s explore how you’re feeling.')}")
        
        render_chat_interface()
        handle_chat_input(model, system_prompt=get_tone_prompt())

# --- 9. SCROLL SCRIPT ---
st.markdown("""
<script>
    function scrollToBottom() {
        var chatContainer = document.querySelector('.chat-container');
        if (chatContainer) {
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    }
    setTimeout(scrollToBottom, 100);
</script>
""", unsafe_allow_html=True) 
