from research_and_blog_crew.crew import researchandblogcrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI agents in developing the Deep Tech business both ways Good and Harmful.'
    }

    try:
        researchandblogcrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
