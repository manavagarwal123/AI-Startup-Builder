from crew import startup_crew

industry = input("Enter startup industry: ")

result = startup_crew.kickoff(
    inputs={"industry": industry}
)

print("\nGenerated Startup Plan:\n")
print(result)