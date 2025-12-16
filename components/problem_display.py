# Logic for displaying problems in Streamlit
import streamlit as st

def display_problems_by_topic(problems_by_topic):
    """
    Display problems organized by topic, with each topic in separate panels.
    Each problem will have an input field, and a Submit button will be provided per panel.
    """
    for topic, problems in problems_by_topic.items():
        with st.expander(f"Topic: {topic}", expanded=True):
            st.write(f"### Problems for {topic}")
            
            user_answers = []

            for i, problem in enumerate(problems):
                col1, col2 = st.columns([8, 2])

                with col1:
                    st.write(f"{i+1}. {problem}")

                with col2:
                    answer = st.text_input(
                        label=f"Answer {i+1} for {topic}",
                        placeholder="Enter your answer",
                        key=f"{topic}_{i}"
                    )
                    user_answers.append(answer)

            # Add a submit button for each panel
            submit_button = st.button(label=f"Submit Answers for {topic}")

            if submit_button:
                st.write(f"Submitted answers for {topic}: {user_answers}")

# Example usage
if __name__ == "__main__":
    example_problems = {
        "Algebra": ["Solve for x: 2x + 5 = 15", "Simplify: (x + 2)^2"],
        "Geometry": ["Find the area of a triangle with base 5 and height 4."]
    }

    display_problems_by_topic(example_problems)
