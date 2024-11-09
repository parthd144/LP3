def job_sequencing(jobs, n):
    # Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x[1], reverse=True)

    # Create an array to keep track of free time slots
    result = [False] * n  # Track which slots are filled
    job_sequence = ['-1'] * n  # Store job sequence

    # Iterate through all given jobs
    for job in jobs:
        job_id, profit, deadline = job
        # Find a slot for this job, checking from the last possible slot
        for j in range(min(n, deadline) - 1, -1, -1):
            if not result[j]:
                result[j] = True
                job_sequence[j] = job_id
                break

    # Filter out unused slots and return the sequence
    return [job_id for job_id in job_sequence if job_id != '-1']

# User input
num_jobs = int(input("Enter the number of jobs: "))

jobs = []
print("Enter job details in the format 'JobID,Profit,Deadline' (one job per line):")
for _ in range(num_jobs):
    job_input = input().split(',')
    job_id = job_input[0].strip()
    profit = int(job_input[1].strip())
    deadline = int(job_input[2].strip())
    jobs.append((job_id, profit, deadline))

# Maximum deadline (used as the size of slots array)
max_deadline = max(job[2] for job in jobs)

# Get the job sequence for maximum profit
optimal_sequence = job_sequencing(jobs, max_deadline)
print(f"The optimal job sequence is: {optimal_sequence}")
