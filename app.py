import streamlit as st
import os
from dotenv import load_dotenv
import groq

# --- Configuration ---
PAGE_TITLE = "TM Camino Chatbot"

# --- Load Environment Variables ---
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
secret_code = os.getenv("SECRET_CODE")
groq_model = os.getenv("GROQ_MODEL")

# --- Basic Styling ---
st.set_page_config(page_title=PAGE_TITLE, page_icon="icon.png", layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.title(PAGE_TITLE, anchor=None)
st.caption(f"<span class='caption'>De Thomas More AI-assistent voor de Camino 2025</span>", unsafe_allow_html=True)

# --- Secret Code Access ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    entered_code = st.text_input(
        "Voer de geheime code in om de chatbot te gebruiken:",
        type="password",
        key="secret_code_input"
    )
    if entered_code:
        if entered_code == secret_code:
            st.session_state.authenticated = True
            # Clear the input field after successful authentication
            st.rerun() # Rerun to hide the input field and show the chat
        else:
            st.error("Ongeldige code. Probeer het opnieuw.")
            st.stop() # Stop execution if code is wrong
    else:
        st.info("Voer de geheime code in om verder te gaan.")
        st.stop() # Stop execution until code is entered

# --- Chatbot Logic (only if authenticated) ---
if st.session_state.authenticated:
    # Check for API key after authentication
    if not api_key or api_key == "YOUR_GROQ_API_KEY_HERE":
        st.error("Groq API sleutel niet gevonden of niet ingesteld in .env bestand. Controleer uw .env bestand.")
        st.stop()
    if not secret_code or secret_code == "YOUR_SECRET_CODE_HERE":
         st.warning("De geheime code is nog de standaardwaarde. Stel een unieke code in het .env bestand in.")
         # Allow continuation but warn the user
    if not groq_model or groq_model == "YOUR_GROQ_MODEL_HERE":
        st.error("Groq model niet gevonden of niet ingesteld in .env bestand. Controleer uw .env bestand.")
        st.stop()

    try:
        client = groq.Groq(api_key=api_key)
    except Exception as e:
        st.error(f"Fout bij het initialiseren van de Groq client: {e}")
        st.stop()

    # System Prompt for Camino Catbot
    system_prompt = {
        "role": "system",
        "content": """Je bent 'Camino Catbot', een behulpzame, ervaren gids, gespecialiseerd in de Camino de Santiago (ook bekend als de Sint-Jakobsroute of de Pelgrimsroute naar Compostella).
        Je spreekt vloeiend Nederlands en bent gespecialiseerd in het helpen van pelgrims die de Camino de Santiago willen bewandelen.
        Je kennis omvat, maar is niet beperkt tot:
        - Beperk je antwoorden tot Santiago de Compostela in Spanje en NIET tot andere steden of regio's met de naam Santiago.
        - De geschiedenis van de Camino.
        - De verschillende routes (Camino Francés, Camino Portugués, Camino del Norte, Via de la Plata, Camino Primitivo, Camino Inglés, etc.).
        - Belangrijke steden, dorpen en bezienswaardigheden langs de routes.
        - Praktische tips voor pelgrims (voorbereiding, paklijst, accommodaties/albergues, pelgrimspaspoort/credencial, compostela).
        - Culturele en spirituele aspecten van de pelgrimstocht.
        - Veelvoorkomende uitdagingen en hoe ermee om te gaan.
        - Indien de input het woord "vertaal" bevat, geef de Spaanse vertaling van de ingevoerde tekst.
        - De rol van pelgrims in de geschiedenis en cultuur van Spanje.
        - **VERTEL NOOIT** onjuiste of misleidende informatie over de Camino de Santiago.
        Antwoord altijd in het Nederlands. Wees vriendelijk, informatief en geduldig. Geef gedetailleerde antwoorden waar mogelijk. Formatteer je antwoorden duidelijk, gebruik bijvoorbeeld lijsten of paragrafen waar nodig.
        """
    }

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Stel je vraag over de Camino:"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Prepare messages for Groq API
        messages_for_api = [system_prompt] + st.session_state.messages

        try:
            # Get assistant response
            chat_completion = client.chat.completions.create(
                messages=messages_for_api,
                model=groq_model,
                temperature=0.2,
                max_tokens=4160,
                top_p=1,
                stop=None,
                stream=False, # Set to True for streaming response
            )
            response_content = chat_completion.choices[0].message.content

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(response_content)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response_content})

        except Exception as e:
            st.error(f"Er is een fout opgetreden bij het communiceren met de Groq API: {e}")
