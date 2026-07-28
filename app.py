import streamlit as st
import os
from dotenv import load_dotenv

from agents.router import route_user_query
from agents.testcase_agent import generate_test_cases
from agents.rag_agent import answer_qa_question
from agents.review_agent import review_and_refine_output

load_dotenv()


st.set_page_config(
    page_title="Agentic QA AI Assistant",
    layout="wide"
)

seamless_dark_css = """
<style>

header[data-testid="stHeader"] {
    background-color: transparent !important;
    z-index: 1;
}


header[data-testid="stHeader"] * {
    color: #ffffff !important;
}


.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%) !important;
    color: #f8fafc !important;
}


footer {
    visibility: hidden;
    height: 0px;
}


.main .block-container {
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
}


[data-testid="stSidebar"] {
    background-color: #020617 !important;
    border-right: 1px solid #1e293b;
}

[data-testid="stSidebar"] * {
    color: #f1f5f9 !important;
}


[data-testid="stSidebar"] code {
    background-color: #1e293b !important;
    color: #38bdf8 !important;
}


h1, h2, h3, h4 {
    color: #ffffff !important;
    font-weight: 700 !important;
}


.stAlert {
    background-color: #1e293b !important;
    border: 1px solid #3b82f6 !important;
    color: #f8fafc !important;
    border-radius: 10px !important;
}


.stCaption, [data-testid="stMarkdownContainer"] p {
    color: #e2e8f0 !important;
}


table {
    background-color: #1e293b !important;
    color: #ffffff !important;
    border-radius: 8px !important;
    overflow: hidden;
}

th {
    background-color: #334155 !important;
    color: #38bdf8 !important;
}


div[data-testid="stChatInput"] {
    background-color: #1e293b !important;
    border: 1px solid #6366f1 !important;
    border-radius: 12px !important;
}

div[data-testid="stChatInput"] textarea {
    color: #ffffff !important;
}


.stButton>button {
    background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
    color: #ffffff !important;
    border-radius: 8px;
    border: none;
    font-weight: 600;
    padding: 0.5rem 1rem;
    transition: all 0.2s ease;
}

.stButton>button:hover {
    box-shadow: 0 4px 14px rgba(99, 102, 241, 0.5);
}
</style>
"""

st.markdown(seamless_dark_css, unsafe_allow_html=True)


st.markdown("""
<div style="background: rgba(30, 41, 59, 0.7); padding: 22px; border-radius: 15px; border: 1px solid #334155; margin-bottom: 25px;">
    <h1 style="margin:0; font-size: 2.2rem; color: #ffffff;"> Agentic QA AI Assistant</h1>
    <p style="margin-top: 5px; color: #94a3b8; font-size: 1rem;">AI-Powered Test Case Generator & QA Knowledge Assistant with RAG Architecture</p>
</div>
""", unsafe_allow_html=True)


with st.sidebar:
    st.header("Configuration")
    st.info(" Active Agents:\n- Router Agent\n- Test Case Agent\n- QA Knowledge Agent\n- Review Agent")
    
    st.divider()
    st.subheader(" Dataset Details")
    pdf_dir = "data/pdfs"
    if os.path.exists(pdf_dir):
        pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
        st.write(f"Loaded PDFs: `{len(pdf_files)}`")
        for pdf in pdf_files:
            st.caption(f" {pdf}")
    else:
        st.warning("No PDF folder found.")
        
    st.divider()
    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your QA AI Assistant. Ask me a QA concept question or paste a requirement to generate test cases!"}
    ]


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "sources" in msg and msg["sources"]:
            with st.expander("Sources Retrieved"):
                for src in msg["sources"]:
                    st.caption(f"- {src}")


user_input = st.chat_input("Ask a question (e.g., 'What is STLC?') or request test cases...")

if user_input:
   
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    
    with st.chat_message("assistant"):
        with st.status("Agentic Pipeline Processing...", expanded=True) as status:
            
            
            st.write("Router Agent:Analyzing query intent...")
            intent = route_user_query(user_input)
            st.write(f" Detected Intent: `{intent}`")
            
           
            if intent == "TESTCASE":
                st.write("Test Case Agent:Generating test cases...")
                raw_response = generate_test_cases(user_input)
                sources = []
            else:
                st.write(" QA Knowledge Agent: Searching ChromaDB Vector Store...")
                raw_response, sources = answer_qa_question(user_input)
                
          
            st.write(" Review Agent: Reviewing and polishing output...")
            final_response = review_and_refine_output(user_input, raw_response, intent)
            
            status.update(label="Response Generated Successfully!", state="complete", expanded=False)

      
        st.markdown(final_response)
        
        
        if sources:
            with st.expander("Sources Retrieved"):
                for src in sources:
                    st.caption(f"- {src}")

       
        st.session_state.messages.append({
            "role": "assistant", 
            "content": final_response,
            "sources": sources
        })