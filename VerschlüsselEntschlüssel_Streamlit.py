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
footer = """
# Custom HTML for Footer
footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: var(--background-color);
        color: var(--text-color);
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .footer-link {
        color: var(--text-color);
        text-decoration: none;
    }
    .footer-link:hover {
        text-decoration: underline;
    }
    </style>
    <div class="footer">
        © | Made with <span style="color: red;">♥</span> by <a href="https://github.com/tanishpoddar" target="_blank" class="footer-link">Tanish Poddar</a>
    </div>
"""

# Display Footer
st.markdown(footer, unsafe_allow_html=True)

# Theme adaptation
st.markdown(
    """
    <style>
    :root {
        --background-color: #ffffff;
        --text-color: #000000;
    }
    [data-theme="dark"] {
        --background-color: #0e1117;
        --text-color: #f8f8f2;
    }
    </style>
    """,
    unsafe_allow_html=True
)
