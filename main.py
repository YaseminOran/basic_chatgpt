from gpt import ask_gpt

from prompt_text import prompt

def main():
    while True:
        user_message = input("Lütfen bir mesaj girin (sohbeti sonlandırmak için 'çıkış' yazın): ")
        if user_message.lower() == "çıkış":
            print("Sohbet sonlandırıldı. Görüşmek üzere!")
            break
        response_message = ask_gpt(user_message, prompt)
        print(response_message)


if __name__ == "__main__":
    main()
