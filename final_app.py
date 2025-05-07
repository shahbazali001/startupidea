import uuid
import markdown
import streamlit as st  
import os
import google.generativeai as genai



#Main Page settings 
st.set_page_config(page_title="Startup Idea Generator", page_icon=":rocket:", layout="wide")
st.title("🚀 Incubation Center 🚀")
#Page session state management
if "page" not in st.session_state:
    st.session_state.page = "Landing"
    
def load_Gemini_API_Key():
    try:
        return st.secrets["Google_API_KEY"]
    except Exception as e:
        st.error("Error in loading API key from .streamlit/secrets.tml. Please ensure secrets.toml is configured.")
        return None

def startup_idea_generator(prompt):
    api_key = load_Gemini_API_Key()
    if not api_key:
        return None
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating response either Key or Gemini API: {e}")
        return None    

def main_page():
    st.set_page_config(page_title="Startup Idea Generator", page_icon=":rocket:", layout="wide")
    st.title("🚀 Incubation Center 🚀")
    
    st.markdown("""
    ## 🚀 Turn Ideas into Startups with the Power of AI

    This app is your launchpad to innovation — built for aspiring entrepreneurs to generate complete startup plans using Generative AI.
    ### 🧭 How to Get Started:
    - Use the **sidebar** to open the Startup Idea Generator.
    - Enter a problem or theme you're passionate about.
    - Let **Gemini AI** craft a detailed, actionable startup plan just for you.
    ---
    """)
    
    
    if st.button("Go to Startup Idea Generator"):
        st.session_state.page = "Startup Generator"
        st.rerun()
    
    st.markdown("----")
    st.markdown("## 🚀 Startup Idea Generation Developed By Shahbaz Ali")

#Next Page: Startup Idea Generator
def startup_generator_Page():
    st.title("Startup Idea Generator")
    st.markdown("Enter a problem you're solving or select optional themes to generate a startup plan.")
    #User Interface for user input
    with st.form(key="startup_form"):
        problem = st.text_area(
            "Describe the problem you're trying to solve (e.g., 'Lack of affordable healthcare in rural areas')",
            placeholder="Enter a detailed problem statement..."
        )
        themes = st.multiselect(
            "Select themes (optional)",
            options=["Sustainability", "Healthcare", "Education", "FinTech", "E-Commerce", "Agritech", "Smart Cities", "AI & ML", "Social Impact"],
            help="Choose themes to guide your startup idea."
        )        
        submit_button = st.form_submit_button("Generate Startup Plan")
    if submit_button:
        if not problem and not themes:
            st.warning("Please provide a problem statement or select at least one theme.")
        else:
            # Design prompt for Gemini API
            prompt = f"""
            You are an expert startup consultant and entrepreneur. Your task is to develop a comprehensive, actionable, and investor-ready startup plan based on the following problem or theme:

            **Problem Statement {problem if problem else 'Not provided'} / Theme**: {', '.join(themes) if themes else 'None selected'}

            Act as if you are advising a founder from idea to execution. Cover every critical area required to make this startup successful and profitable.

            Please include the following sections in your response, each as a markdown-formatted heading:

            # 1. Problem Overview
            Clearly define the core problem or unmet need.

            # 2. Proposed Solution
            Describe your product or service that solves the problem.

            # 3. Market Research
            Summarize the current market landscape, trends, and demand.

            # 4. Target Audience
            Define the ideal customer persona(s) and their pain points.

            # 5. Unique Value Proposition
            What differentiates your solution from others?

            # 6. Competitive Analysis
            Identify main competitors and highlight your competitive edge.

            # 7. Business Model
            Explain how the startup will operate and generate revenue.

            # 8. Go-To-Market Strategy
            Outline the strategy for acquiring your first 100–1000 customers.

            # 9. Marketing & Sales Strategy
            Detail your marketing channels, content plan, and sales funnel.

            # 10. Revenue Streams
            Describe all monetization strategies.

            # 11. Tech Stack (if applicable)
            List the tools, platforms, and technologies required.

            # 12. Financial Projections
            Estimate startup costs, revenue, and break-even timeline.

            # 13. Team & Roles
            Suggest key roles and team structure for success.

            # 14. Legal & Compliance
            Mention any legal, regulatory, or compliance considerations.

            # 15. Scalability & Growth Plan
            Explain how you plan to grow and scale the business.

            # 16. Risks & Mitigation Strategies
            List potential risks and how they will be addressed.

            # 17. Funding Strategy
            State how much capital is needed, and ideal investor profile.

            Respond only in well-structured markdown for clarity and readability.
            """
            
            with st.spinner("your startup plan is in progress..."):
                response = startup_idea_generator(prompt)
                if response:
                    st.markdown("# Here is Your Startup Plan #")
                    st.markdown(response)
                else:
                    st.error("Provided Parameter for a successfull Idea are not sufficient.")


def footer():
    st.markdown("""
    <hr style='margin-top: 2em;'>
    <p style='text-align: center; color: grey;'>Startup Implementations Ideas Team</p>
    """, unsafe_allow_html=True)


def main_page():
    st.markdown("""
    ## 🚀 Turn Ideas into Startups with the Power of AI

    This app is your launchpad to innovation — built for aspiring entrepreneurs to generate complete startup plans using Generative AI.
    ### 🧭 How to Get Started:
    - Use the **sidebar** to open the Startup Idea Generator.
    - Enter a problem or theme you're passionate about.
    - Let **Gemini AI** craft a detailed, actionable startup plan for you.
    ---
    """)

    st.info("Go to Idea Generation for startup ideas!")
    #st.button("Generate Startup Idea", key="generate_idea", on_click)
    if st.button("Go to Startup Idea Generator"):
        st.session_state.page = "Startup Generator"
        st.rerun()
    
    st.markdown("----")
        
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Landing", "Startup idea Generator"], index=0 if st.session_state.page == "Landing" else 1)
    if page != st.session_state.page:
        st.session_state.page = page
        st.rerun()

    # Move to Pages basis of session state
    if st.session_state.page == "Main Page":
        main_page()
    elif st.session_state.page == "Startup idea Generator":
        startup_generator_Page()
    # footer on all pages
    st.markdown("## 🚀 Startup Idea Generation Developed By Shahbaz Ali")
    footer()
    

if __name__ == "__main__":
    main_page()
    

    
  
    
