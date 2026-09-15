Warehouse Visibility and Truck Scheduling Platform - Foundation for an Agentic TMS

Client: Bloem, LLC

Project Team: Kevin Dam, CK Thang, Emmit Miller

Team Description

Summary of Technical Strengths

Kevin Dam: Kevin is a Computer Science major with a minor in Cybersecurity. Through his coursework and professional experience, he has gained experience with Python, SQL, Linux, data processing, automation, and software development. His internship experience has included developing Python-based data workflows and automating recurring business processes. These experiences have strengthened his skills in back-end development, data handling, automation, documentation, and working with structured business requirements. He also has experience with databases and web development concepts through his computer science coursework.

CK Thang: CK Thang is a Senior Computer Science major. He has experience with full-stack web development across front-end in React, Next.js and Typescript, along with server side API design, relational database design, and cloud-hosted backends like Firebase. His project experience includes building a full-stack Next.js application integrating Claude API, a cross-platform Flutter app with a Firestore data model supporting real-time synchronization, and a multithreaded Python chat server built from scratch via TCP sockets. These experiences have strengthened his skills in API integration, database design, and building polished front-end interfaces. 

Emmit Miller: Emmit Miller is a Computer Science major with a minor in Theatre. Their strengths lie in languages with similar structures to Python, SQL, Java, and C++, though they’ve gained experience with many more. They have worked heavily with SQL and Python on database work during various internships, which included work on dashboards and dashboard-adjacent projects. Also at those internships, they worked extensively with moving and reporting data, as well as mapping data in one place to data in another. Their minor in Theatre has also taught them many applicable skills, not the least of which include the ability to think well on their feet, how to recognize when and in what way to change direction if needed when a problem requires a different approach, and most importantly how to work to use their unique skills to do their part as best they can while making space for others’ strengths to shine in order to get a project on its feet and make it the best it can possibly be. 
Anticipation of Growth Areas

Kevin Dam: Kevin expects this project to provide additional experience designing and developing a complete full-stack web application. While he has experience with Python, SQL, automation, and data processing, this project will require him to apply Python in a larger web application and gain deeper experience integrating a back-end API with a front-end interface and database. He also expects to gain experience working with React, designing APIs, and developing a system where shipment, scheduling, and carrier-booking information moves between different parts of the application. Another area of growth will be learning more about logistics and transportation-management workflows so that technical decisions accurately reflect Bloem's business processes.

CK Thang: This project pushes the team beyond their current experiences in several ways. The Python/TypeScript backend with Postgres calls for deeper growth in production grade database design at scale. Also with handling real-world, WMS data extracts, validation, transformation, and building reliable pipelines from external sources rather than a self contained dataset. The carrier booking workbench is a new challenge where formatting data and building interface with third-party customer TMS portals, which requires the team to learn unfamiliar logistics workflows and automation techniques not yet used. The scheduling calendar also demands growth in time-based, concurrency logic, a step up from CRUD style data flows in past work. Since this system is meant to be the foundation for a future agentic TMS, the team will need to sharpen API design discipline and documentation practices to a professional standard. 

Emmit Miller: Even in projects which were in service of creating dashboards, most of Emmit’s experience is with backend development. The majority of their work has been in connecting the data with visual frameworks that already had some meat on their bones, then working to make improvements or additions to the visuals from there, so they are anxiously excited to help build the more visual/front-end parts of this project from scratch. It is something that they have not gotten the chance to do as often as they have backend work, and they are excited to learn more of the nuances of making the parts of the project that most people see. This will also be the first time Emmit is working with React. They are no stranger to learning new programming languages, however, learning a new language for the purpose of creating the front-end of a dashboard is admittedly a little daunting. That being said, they also find a certain thrill in flexing a skill they haven’t had as much of a chance to develop using an unfamiliar language, because it significantly lowers the odds of potentially having to swim upstream against prior experience in different, more backend-oriented areas of React, as they have in the past with languages that they had more experience in such as Java. 



Project Description

Background

Bloem, LLC is a West Michigan-based consumer lawn and garden manufacturer whose products are sold through major retailers including Walmart, Lowe's, Home Depot, ACE, and Menards. Bloem ships high volumes of truckload and less-than-truckload freight from its warehouses. Currently, truck scheduling and carrier booking are handled primarily through email and customer transportation management system (TMS) portals.

The goal of this project is to develop a logistics visibility and truck-scheduling web application that operates on top of Bloem's existing warehouse management system (WMS) data. The application will provide shipment visibility, pickup scheduling, and a centralized carrier-booking workflow.

The project will also establish a foundation for Bloem's longer-term goal of developing an agentic TMS that could autonomously schedule and book trucks. Because this capstone project focuses on establishing that foundation, the system will emphasize a clean data model, well-documented APIs, and a maintainable application architecture that can support future automation.

Description of Intended Features / Product Backlog

The initial product backlog consists of the following major features:

Shipment Visibility Dashboard

Display read-only WMS data for outbound orders and loads provided by Bloem.
Provide a centralized view of relevant shipment and load information.
Allow users to search and filter shipment information.

Dock/Pickup Scheduling Calendar

Provide a calendar interface for viewing scheduled warehouse pickups.
Allow users to create and manage pickup appointments.
Associate pickup appointments with relevant shipments or loads.
Provide visibility into upcoming warehouse scheduling activity.



Carrier-Booking Workbench

Allow users to prepare carrier-booking requests using shipment information.
Generate draft carrier-booking emails.
Generate portal-ready load data for customer TMS portals.
Track booking requests and their current status.

WMS Data Integration

Process read-only WMS data extracts supplied by Bloem.
Transform shipment and order information into a format usable by the application.
Maintain a consistent internal data model for shipments, loads, appointments, and booking requests.

Application API

Develop documented API endpoints for accessing and managing application data.
Separate front-end functionality from back-end business logic.
Design the API to support future integrations and automation.

Future Agentic TMS Foundation

Structure the application's data and APIs to support future automated scheduling and carrier-booking capabilities.
Maintain clear separation between shipment data, scheduling, and booking functionality.
Document important workflows and API functionality so the system can be expanded in the future.

The product backlog will serve as an initial roadmap for development and may change throughout the semester as the team receives additional client feedback and progresses through Scrum sprints.

Anticipated Platform / Tooling

The team has agreed to use Python as the primary back-end programming language for the project. Based on the project's requirements and Bloem's platform preferences, the team currently anticipates using the following technologies and development tools:

Python for back-end development, API development, data processing, and application business logic.
React for development of the front-end web application.
PostgreSQL as the relational database if persistent application storage is required.
REST APIs for communication between the front-end, back-end, and future integrations.
HTML/CSS for web interface structure and styling.
GitHub for source control, project documentation, and team collaboration.
Linear for product backlog management, user stories, sprint planning, and tracking development progress.

Additional Python frameworks, libraries, and development tools will be selected as the team further defines the application's architecture and technical requirements with Bloem.

Technical Considerations

Data Integration

The application will depend on read-only WMS data extracts provided by Bloem. The team will need to understand the structure and relationships within this data before designing the application's internal data model. Source WMS information should remain separate from scheduling and booking information generated by the application.

API Design

Because the application is intended to serve as a foundation for future TMS automation, the back-end API should be designed with extensibility in mind. Shipment information, scheduling operations, and booking functionality should be accessible through clearly defined and documented interfaces.

Database Design

The team will need to develop a data model capable of representing shipments, loads, pickup appointments, carrier-booking requests, and related information. Relationships between these entities should be clearly defined to reduce unnecessary duplication and maintain data consistency.

Security and Access

The application should follow appropriate software security practices. User input should be validated, database operations should be performed securely, and access to application functionality should be limited appropriately based on requirements established with Bloem.

Reliability and Data Accuracy

Shipment and scheduling information can affect real-world warehouse operations. The application should accurately represent the WMS data supplied by Bloem and avoid unintentionally changing source information. Carrier-booking requests generated by the system should also be reviewable before being used for external communication or entered into customer TMS portals.

Maintainability

Because the completed application and repository will ultimately be transferred to Bloem, the team will prioritize readable code, consistent development practices, clear documentation, and a maintainable architecture. The system should be understandable and extendable by developers who were not members of the original capstone team.

Relevant Ethical Principles

The following principles from the Software Engineering Code of Ethics and Professional Practice are particularly relevant to this project:

1.01. Accept full responsibility for their own work.

Relevance: We, the programmers in this case, are to accept full responsibility for any and all work we do, regardless of how that work is received or how it makes us look. It also extends to owning the work of the other programmers, to an extent. For instance, if the other programmers approved a certain part of the program but did not directly write any of that code, those programmers are to also accept responsibility for approving it. Accepting responsibility for the full scope of our work, not just the code we made or added to, forces us as developers to think of the project as one whole and cohesive Thing, which in turn makes it easier to call out any potential missteps or misunderstandings when it comes to following this Code.

3.11. Ensure adequate documentation, including significant problems discovered and solutions adopted, for any project on which they work.

Relevance: We are creating a framework that Bloem would like to eventually build upon to create an automated system. If we do not create adequate documentation to make the project as easy to pass off to their tech teams as we can, we have failed them. In most contexts, the code will, at some point, be handed off to someone who will not know or remember the nuances of which blocks of code perform what function, even if that person is just the same developer a week later. Let alone, the tech side of a company that we are just beginning to work with. Though proper documentation is important in any context, this project in particular needs arguably more emphasis than many others on making sure the documentation is solid, considering that unlike most projects, it is unlikely that any of us be working with Bloem to create this automated system, leaving only developers that did not create this initial version/step of the project to move it forward towards its more permanent form.  

3.13. Be careful to use only accurate data derived by ethical and lawful means, and use it only in ways properly authorized.

Relevance: This is a project based almost entirely in data. It would be irresponsible and unethical for us to use any data other than the approved data via the approved sources. Partially just because of the potential for us to make something that is inaccurate and simply does not map to their data, and partially because, should we bake the wrong patterns and throughlines into this project, they could end up with data that is displayed inaccurately because we used math or refresh patterns from a different source. What’s more, if we do not ensure that our assumptions are correct with someone who knows the data better than we do, we could also misidentify a pattern that only exists in the data we’re using to test, for instance, and then use that incorrect assumption to craft features that could then cause inaccurate reports. So, we will be using only officially approved channels for our data hookups, using only the information we know to be true to program this project.

7.03. Credit fully the work of others and refrain from taking undue credit.

Relevance: In the same way that we need to take responsibility for everything we each individually did, we also need to not overstep with that responsibility-taking into taking responsibility for the work that someone else did. Using the same example as before, if one of us only approved and tested the addition of a feature, that same person should not take credit away from the person who developed the code for that portion of the project. A team of developers cannot shine if each developer individually is not credited for their skills and contributions. 

7.04. Review the work of others in an objective, candid, and properly documented way.

Relevance: All group work comes with a certain nervousness around critique, especially considering that we have not known each other for very long. However, it is important to not soften the blow of those critiques to the detriment of communicating what needs to be changed. This is not to say that there can’t be boundaries, or that there isn’t still a line that can be crossed as far as being too mean. For instance, it is not “objective” to throw in a personal insult when reviewing someone’s work on the newest clickable button. Even so, if such a thing were to happen by accident, it is better to have a conversation on how to improve communication outcomes in the future than to not deliver a working product because of the fear of a bad reaction. What’s more, if the reviews include changes that need to be made, the specifics of those additions or critiques should be documented so that the programmer is able to look back at what they need to do or fix, and so that others can see what was said in the review. Allowing others to see is a big deal, both for the safety of the reviewee and reviewer, and for the potential of a third party to catch any inaccurate or poorly-worded critiques before the changes are implemented only to need to be undone. 

8.02. Improve their ability to create safe, reliable, and useful quality software at reasonable cost and within a reasonable time.

Relevance: Coding and program development is a skill, and like any skill, if you rest on your laurels for too long, you can stagnate. What’s more, the industry moves incredibly fast, often in very sudden bursts of progress that have the potential to change the entire landscape in the blink of an eye. If we, as developers, are not curious, and are not earnestly attempting to become better programmers, we will be left in the dust as Progress heaves onward and pulls those willing to embrace it into the future. As this is a project for an academic course, the emphasis on learning is even more pertinent.

8.03. Improve their ability to produce accurate, informative, and well-written documentation.

Relevance: Just as we must chase knowledge and become better programmers, we must also stay up to date with the most recent and communication-efficient documentation. No developer can truly be a good programmer without knowing how to communicate what they made and how it works to those who will work on it after them, and to improve one’s ability to do so is to become a better developer. Again, because this project is for academic purposes, really learning how to best document what we create as best we can in the time allotted is especially important.

8.04. Improve their understanding of the software and related documents on which they work and of the environment in which they will be used.

Relevance: If we do not have a solid understanding of the data, software, languages, etc. that we are working with, we cannot effectively deliver a product that utilizes them in the best way possible for the client. We must be curious and seek more than just the bare minimum that we need to create, so as to make the best possible use of our knowledge and the resources before us. Doing so has the potential to reduce costs, speed up operations, and overall improve morale when the quality of work that they’re interacting with feels sleek and well-made. 

