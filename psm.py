# import streamlit as st

# st.header("Password Strength Meter")

# def password_strength(password):
#     score = 0
#     feedback = []

#     if len(password) >= 8:
#         score += 1
#     else:
#      feedback.append("Password Must Contain At Least 8 Letter or Numbers")


#      if score == 1 :
#         st.success("your Password is 8 letters longs")
#      else:
#         st.error("your password is short")

#     #feedback
#     if feedback:
#         with st.expander("Improve Your Password"):
#             for item in feedback:
#                 st.write(item)

#     password = st.text_input("Enter Your Password:", type="password")

#     if st.button("Check Strength"):
#        if password:
#                password_strength(password)
#     else:
#        st.warning("Please Enter Password First")
              
import re;
import streamlit as st  

st.header("Password Strength Meter")  

def password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must contain at least 8 characters.")

    if re.search(r"[A-Z]" , password) and re.search(r"[a-z]", password):
        score +=1    
    else:
        feedback.append("Password Must Contain Capital And Small Letter Both.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password Must Contain At Least One Number (0-9).") 

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Password Must Contain At Least One Special Character [!@#$%^&*].")                  



    if score == 4:
        st.success("Your password is strong enough.")
    elif score == 3:
        st.info("Moderate Password - Consider Improve Security By Addind More Feature")
    else:
        st.info("**Weak Password*** - Follow The Suggestion Below to Strength It. ")    

    if feedback:
        with st.expander("Improve Your Password"):
            for item in feedback:
                st.write(f"- {item}")

# Streamlit UI components
password = st.text_input("Enter Your Password:", type="password")  

if st.button("Check Strength"):
    if password:
        password_strength(password)
    else:
        st.warning("Please enter a password first.")
