# Spotify Music Trend Analysis

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Project Overview

Spotify Music Trend Analysis is a data analytics project created as part of the Code Institute Data Analytics with AI Hackathon.

Our three-person team is analysing Spotify track data to explore patterns in music popularity and understand how different track characteristics are associated with popularity.

The project will combine Python-based data cleaning, exploratory data analysis and statistical testing with an interactive Tableau dashboard. The aim is to turn the dataset into clear and useful insights that can be understood by both technical and non-technical users.

### Project Objectives

The project aims to:

- Clean and validate the Spotify dataset so it is ready for analysis.
- Compare popularity across different genres.
- Investigate how danceability, energy and duration are associated with popularity.
- Compare the characteristics of the top 20 and bottom 20 tracks by popularity.
- Compare popularity between explicit and non-explicit tracks.
- Test a statistical hypothesis about energy and popularity.
- Present the findings through an interactive Tableau dashboard.
- Clearly document the project process, testing and findings.


## Dataset Content


## Business Requirements

The purpose of the project is to use Spotify track data to investigate music popularity patterns and explore whether different track characteristics are associated with popularity.

The project will answer the following questions:

1. Which genres have the highest and lowest average popularity?
2. How are danceability, energy and duration associated with popularity?
3. What differences can we identify between the top 20 and bottom 20 tracks by popularity?
4. Are explicit tracks more or less popular than non-explicit tracks?

The final dashboard will present the results of these questions in a clear and interactive way.


## Hypothesis and How to Validate It

The project will test whether there is a statistically significant relationship between track energy and popularity.

### Null Hypothesis (H0)

There is no significant relationship between track energy and popularity.

### Alternative Hypothesis (H1)

There is a significant relationship between track energy and popularity.

### Validation Approach

The relationship between energy and popularity will first be explored using descriptive statistics and visualisations.

The distributions of the variables will then be reviewed before selecting an appropriate statistical test.

The result will be interpreted using the strength and direction of the relationship together with statistical significance and the p-value.

Any relationship identified will be described as an association rather than evidence that energy causes a track to become popular.


## Project Plan

The project is being completed over four days using milestones to organise the work.

### Milestone 1 - Day 1: ETL and Initial Analysis

- Define the project scope and research questions.
- Set up the GitHub repository and project board.
- Create and assign project issues and supporting tasks.
- Extract and inspect the Spotify dataset.
- Clean, transform and validate the data.
- Begin initial analysis.

### Milestone 2 - Day 2: Analysis and Dashboard Development

- Analyse genre popularity.
- Analyse danceability, energy and duration.
- Compare the top 20 and bottom 20 tracks.
- Compare explicit and non-explicit tracks.
- Test the energy and popularity hypothesis.
- Begin development of the Tableau dashboard.

### Milestone 3 - Day 3: Testing and Documentation

- Test and validate the ETL and analysis.
- Test the Tableau dashboard.
- Make final dashboard refinements.
- Complete the README and project documentation.
- Prepare the project findings for presentation.

### Milestone 4 - Day 4: Final Presentation and Submission

- Complete final fixes.
- Review project deliverables.
- Complete a presentation dry run.
- Prepare for questions.
- Submit and present the completed project.


## Project Management and Team Roles

The project is being completed by a team of three, with each member having a main area of responsibility while still contributing to the overall project.

### Project Manager

The Project Manager is responsible for:

- Setting up and managing the GitHub Project board.
- Creating project issues, tasks and milestones.
- Assigning and monitoring work.
- Tracking project progress.
- Managing project scope.
- Coordinating team check-ins.
- Building the Tableau dashboard.
- Supporting dashboard testing.
- Coordinating project documentation.
- Coordinating the final presentation.

### Data Architect

The Data Architect is responsible for:

- Data extraction.
- Data cleaning and transformation.
- Data validation.
- Data quality and consistency.
- Preparing the cleaned dataset for analysis.
- Testing the ETL process.

### Data Analyst

The Data Analyst is responsible for:

- Exploratory data analysis.
- Analysing the research questions.
- Statistical analysis.
- Hypothesis testing.
- Producing analytical insights and visualisations.

The team will use shared responsibility and support each other where required.


## Project Tracking

GitHub Projects is being used to manage and track the project.

The project work has been divided into individual issues containing supporting task checklists.

Each issue is assigned to a team member and linked to one of the four project milestones.

The board uses the following workflow:

**Todo, In Progress, Review, Done**

The team will use regular check-ins to review progress, discuss blockers and update the board as work is completed.


## Scope and Prioritisation

The team has prioritised the project so that the core dashboard and analysis are completed before optional features are attempted.

### Must Have

The core project requirements are:

- Clean and validated Spotify dataset.
- Genre popularity analysis.
- Audio feature and popularity analysis.
- Top 20 versus bottom 20 comparison.
- Explicit versus non-explicit comparison.
- Statistical hypothesis test.
- Interactive Tableau dashboard.
- Dashboard testing.
- ETL and analysis testing.
- Complete README and project documentation.
- Final project presentation.

### Should Have

- Additional useful Tableau filters and user controls.

### Could Have

- A simple popularity prediction model if all core project requirements are completed.
- Analysis of additional Spotify audio features if time allows.

### Won't Have

- A Spotify recommendation system.

The recommendation system was kept outside the project scope so that the team could focus on delivering the core ETL, analysis, Tableau dashboard, testing and documentation within the four-day timeframe.


## The Rationale to Map the Business Requirements to the Data Visualisations


## Analysis Techniques Used


## Use of Generative AI


## Ethical Considerations

The project uses track-level Spotify data rather than personal information about individual Spotify users.

Popularity will not be treated as a measure of musical quality or artistic value.

There may also be differences in the number of tracks represented across genres or artists, which could influence comparisons.

Relationships between audio features and popularity will be described as associations rather than proof of causation.

The team will also clearly acknowledge limitations in the dataset and avoid making claims that cannot be supported by the analysis.

The dataset source and any external resources used during the project will be credited appropriately.


## Dashboard Design


## Testing and Validation


## Version Control and Collaboration

GitHub is being used for version control and collaboration throughout the project.

The team will use:

- Separate development branches.
- Regular commits.
- Pull requests.
- Team review before changes are merged.
- GitHub Issues for project tasks.
- GitHub Projects for project tracking.
- Milestones to organise work across the four hackathon days.

Team members will complete work on their own branches before submitting pull requests back to the main project repository.


## Unfixed Bugs


## Challenges and Problem Solving


## Development Roadmap


## Deployment


## Main Data Analysis Libraries


## Project Files


## Credits

### Data

The project uses the Spotify Tracks Dataset provided through Kaggle:

https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset

### Project Guidance

The project was developed as part of the Code Institute Data Analytics with AI Hackathon.

The Code Institute hackathon brief and README template were used to guide the project structure and requirements.

Any additional tutorials, code examples or external resources used during development will be credited here.


## Acknowledgements

We would like to thank Code Institute and our bootcamp facilitators for providing the hackathon brief, guidance and support throughout the project.