import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="Myanmar Text to Speech", page_icon="🔊", layout="centered")

st.title("🇲🇲 မြန်မာစာမှ အသံသို့ ပြောင်းစက် (Free TTS)")
st.write("Credit ကုန်စရာမလိုဘဲ မြန်မာလို ရိုက်ထည့်ကာ အသံဖိုင် (MP3) အခမဲ့ ထုတ်ယူနိုင်ပါပြီ။")

text_input = st.text_area("အသံပြောင်းချင်သော မြန်မာစာသားကို ဤနေရာတွင် ရိုက်ထည့်ပါ သို့မဟုတ် ကူးထည့်ပါ:", 
                          value="မင်္ဂလာပါရှင်။ မြန်မာစာသားကို အသံဖိုင်အဖြစ် အလွယ်တကူ ပြောင်းလဲနိုင်ပါပြီ။", height=150)

if st.button("🔊 အသံထုတ်လုပ်မည် (Generate Audio)", type="primary"):
    if not text_input.strip():
        st.warning("ကျေးဇူးပြု၍ စာသားအနည်းဆုံး တစ်ခုခု ထည့်ပေးပါ။")
    else:
        with st.spinner("အသံဖိုင် ဖန်တီးနေပါပြီ... ခဏစောင့်ပေးပါ။"):
            try:
                tts = gTTS(text=text_input, lang='my', slow=False)
                audio_file = "output.mp3"
                tts.save(audio_file)
                
                st.success("အသံဖိုင် အောင်မြင်စွာ ထွက်လာပါပြီ!")
                st.audio(audio_file, format='audio/mp3')
                
                with open(audio_file, "rb") as file:
                    st.download_button(
                        label="📥 အသံဖိုင် Download ဆွဲရန် (MP3)",
                        data=file,
                        file_name="myanmar_audio.mp3",
                        mime="audio/mp3"
                    )
            except Exception as e:
                st.error(f"မှားယွင်းမှု ရှိပါသည်: {e}")

st.markdown("---")
st.caption("💡 ဤ App ကို GitHub တွင် သိမ်းဆည်းပြီး Streamlit Cloud ဖြင့် အခမဲ့ Host လုပ်ကာ အလွယ်တကူ အသုံးပြုနိုင်ပါသည်။")
