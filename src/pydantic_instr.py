"""
Extracting CV example:
1. Handle environmente error if failed to load env var
2. create a pydantic model with fields
name: str
description optional
education qualifications dictionary with branch, gpa as key and college/university value
projects optional 
experience optional 
skills 
hobbies optional 
interests optional 
3. read the contents from the cv using file reading operations and store everything in a string, if the file is large read in chunks. Handle exceptions like file not exist
4. create an instructor LLM client from provider of choice
5. wrap the create block with response model as pydantic model and string as the messages content.
6. and in exception blocks handle client errors, server errors and generic errors.
7. we can access the output using attributes names in our pydantic model
8. the reason for keeping most of the fields  optional is CVs dont follow a madatory structure and to avoid pipeline breakage, safe to assume most of the fields optional
"""

from datetime import datetime
from typing import Optional

import instructor

# from google import genai
from google.genai import errors
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

PROMPT = "Extract details from the job descriptions"


class JobPost(BaseModel):
    title: str
    company_name: str
    company_overview: Optional[str] = None
    description: str
    required_skills: list[str]
    optional_skills: Optional[list[str]] = None
    location: str
    salary: Optional[str] = None
    posted_date: Optional[datetime] = None


class JobPostings(BaseModel):
    postings: list[JobPost]


post_list: list = [
    """
    Senior Technical Program Manager, Network Infrastructure and Capacity Planning
    Minimum qualifications:
    Bachelor's degree in a technical field, or equivalent practical experience.
    8 years of experience in program management.

    Preferred qualifications:
    8 years of experience managing complex, cross-functional network planning projects.
    Experience integrating AI and automation to streamline workflows and project lifecycles.
    Understanding of financial implications of network expansions and cost-optimization strategies.
    Ability to adapt in dynamic, automation-first environments, with a track record of process improvement.
    Ability to analyze large-scale datasets for capacity, demand, and resource allocation.
    Excellent attention to detail in reviewing AI-generated network topologies, identifying anomalies, and upholding AI principles for responsible deployment.
    About the job
    A problem isn’t truly solved until it’s solved for all. That’s why Googlers build products that help create opportunities for everyone, whether down the street or across the globe. As a Technical Program Manager at Google, you’ll use your technical expertise to lead complex, multi-disciplinary projects from start to finish. You’ll work with stakeholders to plan requirements, identify risks, manage project schedules, and communicate clearly with cross-functional partners across the company. You're equally comfortable explaining your team's analyses and recommendations to executives as you are discussing the technical tradeoffs in product development with engineers.

    The Network Planning, Design, and Solutions team drives the strategic evolution of Google's global infrastructure. We craft comprehensive plans for the WAN Core, Campus, and edge, transforming critical Cloud and product area needs into engineered L3-to-L1 capacity designs. Join us to build the resilient, high-performance networks that enable Google's products and services to reach billions.

    In this role, you will be a key architect in scaling Google's global network infrastructure by strategically planning and designing the future capacity and topology of the WAN Core and Campus networks. This role is critical for meeting the demands of Google Cloud and all product areas by transforming network planning through AI and automation. You will lead the shift to intention-based planning, leveraging AI agents and agentic skills to automate high-volume tasks and generate auto-validated Plans of Record (PORs). This includes using AI-driven models for demand translation and automating the complex L3-to-L1 mapping process, thereby enhancing efficiency and accuracy in network planning.
    The AI and Infrastructure team is redefining what’s possible. We empower Google customers with breakthrough capabilities and insights by delivering AI and Infrastructure at unparalleled scale, efficiency, reliability and velocity. Our customers include Googlers, Google Cloud customers, and billions of Google users worldwide.

    We're the driving force behind Google's groundbreaking innovations, empowering the development of our cutting-edge AI models, delivering unparalleled computing power to global services, and providing the essential platforms that enable developers to build the future. From software to hardware our teams are shaping the future of world-leading hyperscale computing, with key teams working on the development of our TPUs, Vertex AI for Google Cloud, Google Global Networking, Data Center operations, systems research, and much more.

    The US base salary range for this full-time position is $192,000-$278,000 + bonus + equity + benefits. Our salary ranges are determined by role, level, and location. Within the range, individual pay is determined by work location and additional factors, including job-related skills, experience, and relevant education or training. Your recruiter can share more about the specific salary range for your preferred location during the hiring process.

    Please note that the compensation details listed in US role postings reflect the base salary only, and do not include bonus, equity, or benefits. Learn more about benefits at Google.

    Responsibilities
    Drive WAN and Campus network planning transformation by building AI agents to automate manual, high-volume tasks into intention-based Plans of Record (POR).
    Leverage AI models to translate complex network demands into L3 requirements, collaborating with engineering on automated L3-to-L1 mapping for accurate PORs.
    Integrate reusable agentic skills into the planning pipeline, managing deliverables like stockout remediation and geo-expansion while ensuring network supply plan alignment via change control boards.
    Design and optimize automated planning tools and systems of record for scalability, monitoring key metrics to proactively identify and resolve process bottlenecks.
    Lead cross-functional strategy as the liaison between global network delivery, systems, and product, providing technical guidance on AI implementation, data integrity, and optimization.

    """,
    """
    Product Strategy and Operations Principal, AI2 Strategic Partnerships
    Minimum qualifications:
    Bachelor's degree or equivalent practical experience.
    11 years of experience in management consulting, product management and strategy, or analytics in a technology company.
    Experience working with and analyzing data, and managing multiple cross-functional programs or projects.

    Preferred qualifications:
    Master's degree or PhD.
    Experience working with product and engineering teams.
    Strong product sense and understanding of the infra stack.
    Ability to thrive in a fast paced matrixed environment, influence and collaborate cross-functionally with technical leads, engineering fellows, engineering leaders, finance, legal, accounting.
    Excellent written and verbal communication skills.
    About the job
    Product and Business Strategy Leaders bring together teams across Google’s functions to help products execute optimally. Our team pushes Google to scale at key points that refine our products and infrastructure by executing efficiently, bringing solid business sense and sound judgment, and working effectively across organizational lines.

    Our roles often include components of strategy (e.g. analyzing and understanding new trends in the industry, building business plans), operations (e.g. running the cadence of organizations, connecting the operating lines between our functions), and communications. Our team partners with senior leadership to run important functions that cross-cut our existing organizations and deliver high impact projects. We help Engineers, PMs, UX, and all of our other functions to build amazing products that delight our users, and then get those products into their hands.

    In this role, you will work with the Office of Alphabet's CEO and AI2’s executive leadership to drive the strategic partnerships on various strategic topics including supply discussions, technology collaborations, partnership announcements, etc. You will act as the single source of truth and lead these efforts to ensure the Partner Engagement with AI2 leadership is efficient and impactful based on the strategic positioning defined by AI2 and Alphabet leadership. AI2 leadership has clear context based on internal and external research/assessment and is fully debriefed on relevant context before engaging with partners. AI2 partner engagement is aligned with the rest of Alphabet (e.g. broader Cloud) in terms of messaging, announcements, etc.

    The US base salary range for this full-time position is $177,000-$257,000 + bonus + equity + benefits. Our salary ranges are determined by role, level, and location. Within the range, individual pay is determined by work location and additional factors, including job-related skills, experience, and relevant education or training. Your recruiter can share more about the specific salary range for your preferred location during the hiring process.

    Please note that the compensation details listed in US role postings reflect the base salary only, and do not include bonus, equity, or benefits. Learn more about benefits at Google.
    Responsibilities
    Identify problems and issues across the organization and define/lead programs and processes to solve them.
    Influence team members and executive management to act and drive projects to completion.
    Establish and lead operating processes and tools for effectively managing the organization and achieving goals.
    Shape the partnership strategy and establish governance structures/operating models to maximize value for Alphabet.
    Facilitate the discussion between Alphabet/AI2 leadership and strategic partners by building clear artifacts and communications.

    """,
    """
    Customer Engineering Manager IV, Google Cloud
    Minimum qualifications:
    Bachelor's degree or equivalent practical experience.
    10 years of experience with cloud native architecture in a customer-facing or support role.
    Experience in leadership (e.g., people management, team lead, mentorship, coaching).
    Experience with cloud engineering, on-premise engineering, virtualization, or containerization platforms.
    Experience with technical conversations, demos, prototyping, or workshops with customers.

    Preferred qualifications:
    Experience with software lifecycles, building tools, and architecting/developing software for scalable, distributed systems (e.g., data platform, AI/ML, infrastructure).
    Experience as a pre-sales manager or technical customer-facing people manager within a professional services or sales engineering team.
    Experience managing a team through pre-sales processes and career development (e.g., account mapping, quota setting, performance management, managing sensitive information).
    Experience engaging with, and presenting to, technical stakeholders/executive leaders (e.g., delivering compelling messages by audience, asking strategic questions, leading conversations that drive accelerated value realization and business opportunity).
    Experience driving delivery and consumption plans for complex, cross-pillar cloud solutions.
    About the job
    As a Customer Engineering (CE) Manager, you will lead and deploy a team of subject matter experts responsible for working alongside our customers to provide trusted technical and solution advice to accelerate workload migration and remove technical blockers. You will foster a culture of technical ownership and understand the mechanics of architecture, delivery, and consumption across the Google Cloud portfolio.

    Google Cloud accelerates every organization’s ability to digitally transform its business and industry. We deliver enterprise-grade solutions that leverage Google’s cutting-edge technology, and tools that help developers build more sustainably. Customers in more than 200 countries and territories turn to Google Cloud as their trusted partner to enable growth and solve their most critical business problems.

    The US base salary range for this full-time position is $192,000-$267,000 + bonus + equity + benefits. Our salary ranges are determined by role, level, and location. Within the range, individual pay is determined by work location and additional factors, including job-related skills, experience, and relevant education or training. Your recruiter can share more about the specific salary range for your preferred location during the hiring process.

    Please note that the compensation details listed in US role postings reflect the base salary only, and do not include bonus, equity, or benefits. Learn more about benefits at Google.

    Responsibilities
    Lead a team of Customer Engineers, focusing on team culture, talent strategy, and skills development to deliver successful cloud transformation outcomes for customers and accelerate value realization.
    Foster customer partnership and provide thought leadership related to cloud, cross-pillar solutions, and expansion opportunities to drive technical wins.
    Partner with Sales to define technical go-to-market strategies and delivery plans, with a focus on winning new workloads and driving consumption within existing ones.
    Balance technical leadership with operational excellence; lead workload and opportunity review meetings and provide insight into how to achieve a technical agreement and migration strategy, working directly with our customers, partners, and prospects.
    Work cross-functionally across Google, partners, and team to resolve technical roadblocks.
                
    """,
]

message_str: str = ""

for i, j in enumerate(post_list):
    message_str += f"\n{i+1}. {j}"


client = instructor.from_provider("google/gemini-3-flash-preview")

try:
    Job_posting = client.create(
        response_model=JobPostings,
        messages=[
            {
                "role": "user",
                "content": PROMPT + message_str,
            }
        ],
        max_retries=3,
    )

    for i, j in enumerate(Job_posting.postings):
        print(f"\n{i+1}.\n{j}")

except errors.ClientError as e:
    if e.code == 429:
        print("Rate limited..")

except errors.ServerError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")
