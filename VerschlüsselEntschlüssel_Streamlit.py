import streamlit as st
import base64
def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        list_key = key[i % len(key)]
        list_enc = chr((ord(msg[i]) + ord(list_key)) % 256)
        enc.append(list_enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
def decode(key, code):
    dec = []
    enc = base64.urlsafe_b64decode(code).decode()
    for i in range(len(enc)):
        list_key = key[i % len(key)]
        list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)
        dec.append(list_dec)
    return "".join(dec)
st.title("Verschlüssel Entschlüssel")
st.subheader("Made By:")
st.text("Tanish Poddar [RA2311003010959]")
st.write("### Type Your Message:")
msg = st.text_input("Message", key="msg")
st.write("### Enter The Key:")
key = st.text_input("Key", key="key")
st.write("### Choose one of Encryption or Decryption:")
mode = st.radio("", ("Encryption", "Decryption"), key="mode")
if st.button("Show Message!", key="show_button"):
    if msg and key:
        if mode == "Encryption":
            result = encode(key, msg)
        else:
            result = decode(key, msg)
        st.write("### Result:")
        st.text(result)
    else:
        st.error("Please enter both the message and the key.")
if st.button("Reset", key="reset_button"):
    st.experimental_rerun()
st.markdown("<p style='text-align: center;'>© | Made with ♥ by <a href='https://github.com/tanishpoddar' target='_blank' style='color: inherit; text-decoration: none;'>Tanish Poddar</a></p>", unsafe_allow_html=True)
