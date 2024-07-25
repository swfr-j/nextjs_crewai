from job_manager import append_event


class CompanyResearchCrew:
    def __init__(self, job_id: str):
        self.job_id = job_id
        self.crew = None

    def setup_crew(self, companies: list[str], positions: list[str]):
        print(
            f"Setting up job {self.job_id} with companies {companies} and positions {positions}"
        )

        # TODO: Setup agents

        # TODO: Setup Tasks

        # TODO: Setup the crew

    def kickoff(self):
        if not self.crew:
            raise Exception("Crew not setup")

        append_event(self.job_id, "CREW STARTED")
        try:
            print(f"Running the crew {self.job_id}")
            results = self.crew.kickoff()
            append_event(self.job_id, "CREW COMPLETED")
            return results
        except Exception as e:
            print(f"Error running crew {self.job_id}: {e}")
            append_event(self.job_id, f"CREW ERROR: {e}")
            return None
