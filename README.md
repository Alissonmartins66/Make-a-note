# Voice Assistant

Este é um simples assistente de voz desenvolvido em Python que permite a anotação de texto em um bloco de notas por meio de comandos de voz. O programa inicia quando o usuário diz uma das palavras-chave: "make a note", "write this down" ou "remember this". O assistente captura a fala do usuário, anota a entrada em um arquivo de texto e encerra. Uma solução prática para registrar pensamentos ou notas de forma rápida e sem digitar.

**Recursos:**
- Captura de áudio usando a biblioteca SpeechRecognition
- Síntese de voz para interações usando a biblioteca gTTS (Google Text-to-Speech)
- Anotação de texto em um arquivo de notas
- Comandos de voz intuitivos para iniciar a anotação
- Encerra automaticamente após a anotação

**Instruções de Uso:**
1. Execute o programa e aguarde pelo prompt de voz.
2. Diga uma das palavras-chave para iniciar a anotação: "make a note", "write this down" ou "remember this".
3. Fale o que você deseja anotar.
4. O assistente registrará a anotação em um arquivo de texto e encerrará após alguns segundos após não reconhecer mais nenhuma entrada de áudio.

**Requisitos:**
- Python 3.x
- Bibliotecas Python: speech_recognition, gtts (Google Text-to-Speech), pygame

Divirta-se com esse assistente de voz para anotações simples e eficazes!
