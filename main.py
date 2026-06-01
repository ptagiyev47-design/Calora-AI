from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from groq import Groq

# API Açarın (Dəyişmədən saxla)
API_KEY = "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"

class CaloraInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Başlıq
        self.add_widget(Label(text="🌟 CALORA AI", size_hint_y=None, height=50, font_size=24))

        # Mesajların görünəcəyi yer
        self.scroll = ScrollView()
        self.chat_history = Label(text="Calora: Salam! Sənə necə kömək edə bilərəm?\n", 
                                  size_hint_y=None, halign='left', valign='top')
        self.chat_history.bind(size=self.update_text_size)
        self.scroll.add_widget(self.chat_history)
        self.add_widget(self.scroll)

        # Yazı yazmaq üçün yer
        self.input_area = TextInput(hint_text="...", multiline=False, size_hint_y=None, height=100)
        self.add_widget(self.input_area)

        # Göndər düyməsi
        self.send_btn = Button(text="Send", size_hint_y=None, height=60, background_color=(0, 0.7, 1, 1))
        self.send_btn.bind(on_release=self.send_message)
        self.add_widget(self.send_btn)

        # Groq Klienti
        self.client = Groq(api_key=API_KEY)
        self.messages = [{"role": "system", "content": "Sən Calorasan, ağıllı və mehriban asistentsən."}]

    def update_text_size(self, *args):
        self.chat_history.text_size = (self.chat_history.width, None)
        self.chat_history.height = self.chat_history.texture_size[1]

    def send_message(self, instance):
        user_text = self.input_area.text.strip()
        if user_text:
            self.chat_history.text += f"\n👤 You: {user_text}\n"
            self.input_area.text = ""
            
            try:
                self.messages.append({"role": "user", "content": user_text})
                completion = self.client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=self.messages
                )
                answer = completion.choices[0].message.content
                self.chat_history.text += f"\n🤖 Calora: {answer}\n"
                self.messages.append({"role": "assistant", "content": answer})
                
                # Səhifəni avtomatik aşağı sürüşdür
                self.scroll.scroll_y = 0
            except Exception as e:
                self.chat_history.text += f"\n❌ Xəta: {str(e)}\n"

class CaloraApp(App):
    def build(self):
        return CaloraInterface()

if __name__ == "__main__":
    CaloraApp().run()


