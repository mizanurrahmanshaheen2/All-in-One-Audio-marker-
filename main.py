import os
from gtts import gTTS

def text_to_mp3(input_text, output_file):
    tts = gTTS(text=input_text, lang='bn')
    tts.save(output_file)
    print(f"MP3 file saved: {output_file}")

def main():
    print("Enter your text (type 'exit' to quit):")

    while True:
        user_input = input("> ")

        if user_input.lower() == "exit":
            break

        output_file = "output.mp3"
        text_to_mp3(user_input, output_file)

if __name__ == "__main__":
    main()
