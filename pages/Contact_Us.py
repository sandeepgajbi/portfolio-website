import streamlit as st
from validate_email_address import validate_email
from send_email import send_email

MESSAGE_MAX_LENGTH = 500


def is_valid_email(user_email):
    return validate_email(user_email)


def main():
    st.header("Contact Me")
    with st.form(key='contact_form'):

        st.subheader("Your email address")
        email = st.text_input(label="Email", key='email')

        st.subheader("Your message")
        message = st.text_area(label="Message", max_chars=MESSAGE_MAX_LENGTH, key='message')
        st.write(f'You wrote {len(message)} characters out of {MESSAGE_MAX_LENGTH}.')

        if st.form_submit_button("Submit"):
            if not is_valid_email(email):
                st.error("Please enter a valid email address.")
            elif len(message) == 0:
                st.error("Please enter a message.")
            elif len(message) > MESSAGE_MAX_LENGTH:
                st.error(f"Message length should not exceed {MESSAGE_MAX_LENGTH} characters.")
            else:
                send_email(email, message)
                st.success("Thank you for your submission! Your message has been sent.")


if __name__ == "__main__":
    main()
