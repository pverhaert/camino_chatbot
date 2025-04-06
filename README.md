# Camino Catbot

Dit is een Streamlit-applicatie voor een AI-chatbot gespecialiseerd in de Camino de Santiago. De chatbot maakt gebruik van de Groq API voor snelle antwoorden.

## Installatie

1.  **Clone de repository (of download de bestanden):**
    ```bash
    git clone https://github.com/pverhaert/camino_chatbot.git
    cd camino_chatbot
    ```
    Als u de bestanden heeft gedownload, navigeer dan naar de map waar `app.py` zich bevindt.

2.  **Maak een virtuele omgeving:**
    Het wordt sterk aanbevolen om een virtuele omgeving te gebruiken om projectafhankelijkheden te isoleren.
    ```bash
    python -m venv .venv
    ```
    (Gebruik `python3` indien nodig op uw systeem)

3.  **Activeer de virtuele omgeving:**
    *   **Windows (Command Prompt/PowerShell):**
        ```bash
        .venv\Scripts\activate
        ```
    *   **macOS/Linux (bash/zsh):**
        ```bash
        source .venv/bin/activate
        ```
    Uw terminalprompt zou nu `(.venv)` moeten tonen.

4.  **Installeer de vereiste packages:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configureer de omgeving:**
    *   Hernoem of kopieer het `.env.example` bestand (indien aanwezig) naar `.env`. Als er geen `.env.example` is, maak dan een nieuw bestand genaamd `.env`.
    *   Open het `.env` bestand en voeg uw Groq API-sleutel en een geheime toegangscode toe:
        ```dotenv
        GROQ_API_KEY="uw_groq_api_sleutel_hier"
        GROQ_MODEL="meta-llama/llama-4-scout-17b-16e-instruct"
        SECRET_CODE="uw_geheime_toegangscode_hier"
        ```
    *   **Belangrijk:** Vervang de placeholder-tekst door uw daadwerkelijke Groq API-sleutel, het Groq-model en een unieke, zelfgekozen geheime code.

6.  **Voeg het favicon toe:**
    *   Plaats een afbeelding genaamd `icon.png` in dezelfde map als `app.py`. Dit wordt gebruikt als het browser-tabblad icoon.

## Gebruik

1.  **Zorg ervoor dat uw virtuele omgeving geactiveerd is.** (Zie stap 3 van de installatie)

2.  **Start de Streamlit-applicatie:**
    ```bash
    streamlit run app.py
    ```

3.  **Open de applicatie:**
    Streamlit zal aangeven op welk lokaal adres de app draait (meestal `http://localhost:8501`). Open deze URL in uw webbrowser.

4.  **Voer de geheime code in:**
    U wordt gevraagd om de `SECRET_CODE` in te voeren die u in het `.env` bestand heeft ingesteld.

5.  **Chat met de Camino Catbot:**
    Na het invoeren van de juiste code, kunt u beginnen met het stellen van vragen over de Camino de Santiago in het Nederlands.
