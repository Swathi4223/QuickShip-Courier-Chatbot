
import streamlit as st

st.set_page_config(page_title="SwiftCourier Bot", page_icon="📦")
st.title("📦 SwiftCourier Support Bot")
st.caption("Ask me to track a parcel, check shipping rates, or ask about delivery times!")

# 1. Mock database of tracking numbers
TRACKING_DATA = {
    "TRK101": "In Transit — Arrived at Hyderabad Hub. Expected delivery: Tomorrow.",
    "TRK102": "Delivered — Signed by recipient at 2:15 PM today.",
    "TRK103": "Out for Delivery — Our courier agent is on the way to your address.",
}

# 2. Bot logic function
def get_bot_response(user_text):
    text = user_text.lower().strip()

    # Check if user entered a known tracking ID
    for trk_id, status in TRACKING_DATA.items():
        if trk_id.lower() in text:
            return f"**Tracking Update ({trk_id}):** {status}"

    # Keyword matching for common courier queries
    if "track" in text:
        return "Please enter your tracking ID (try `TRK101`, `TRK102`, or `TRK103`)."
    elif "rate" in text or "price" in text or "cost" in text:
        return (
            "**Standard Shipping Rates:**\n"
            "- Up to 1 kg: ₹50\n"
            "- 1 kg to 5 kg: ₹120\n"
            "- Above 5 kg: ₹250\n"
            "*(Express next-day delivery adds ₹80)*"
        )
    elif "time" in text or "long" in text or "days" in text:
        return "Standard delivery takes **2–4 business days**. Express delivery arrives the **next business day**."
    elif "pickup" in text or "schedule" in text:
        return "To schedule a pickup, please share your **pickup pincode** and **package weight**."
    elif "hello" in text or "hi" in text:
        return "Hello! 👋 How can I help with your shipment today? You can ask to **track a package**, check **shipping rates**, or ask about **delivery times**."
    else:
        return "I didn't quite catch that. Try asking about **tracking**, **shipping rates**, or **delivery times**!"

# 3. Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! 👋 Welcome to SwiftCourier. Type a tracking ID (like `TRK101`) or ask a question."}
    ]

# 4. Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 5. Handle new user input
if prompt := st.chat_input("Type your message here..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and show bot reply
    reply = get_bot_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
