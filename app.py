import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Uppseekers - Interactive Student Application Engine",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Advanced Custom CSS for dynamic hierarchy and scannability
st.markdown("""
    <style>
    .main-header { font-size: 38px; font-weight: 800; color: #1E3A8A; margin-bottom: 5px; }
    .sub-header { font-size: 18px; color: #4B5563; margin-bottom: 25px; }
    .grade-header { font-size: 28px; font-weight: 700; color: #1E40AF; background: #EFF6FF; padding: 10px 15px; border-radius: 8px; margin-top: 20px; }
    .month-card { background: #FFFFFF; border: 1px solid #E5E7EB; border-left: 5px solid #2563EB; padding: 18px; border-radius: 8px; margin-bottom: 15px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .week-title { font-weight: 700; color: #0F172A; font-size: 15px; margin-top: 8px; }
    .pill-counselor { background-color: #ECFDF5; color: #065F46; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }
    .pill-ops { background-color: #FFFBEB; color: #92400E; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }
    .pill-value { background-color: #F5F3FF; color: #5B21B6; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="main-header">🌐 Uppseekers Dynamic Admissions Journey Matrix</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">A transparent, counselor-led profile blueprint mapping granular week-on-week execution directly to top-tier university expectations.</div>', unsafe_allow_html=True)

# --- SIDEBAR STRATEGIC FILTERING ---
st.sidebar.header("📋 Student Profile Parameters")
selected_grade = st.sidebar.selectbox(
    "Select Current Enrollment Grade:",
    options=["Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔍 Dashboard Navigation Info")
st.sidebar.info(
    "Selecting a grade instantly customizes your journey. It starts with your rapid 7-day onboarding launchpad, followed by full month-by-month, week-by-week program tracks running all the way through Grade 12 graduation."
)

# --- PHASE 1: CONDENSED 7-DAY ONBOARDING & ICP ENGINE ---
st.markdown("## ⚡ Phase 1: The High-Velocity 7-Day Onboarding & ICP Framework")
st.markdown("*Mandatory initial launchpad to audit, benchmark, and structurally map out student profiles before entering the weekly track.*")

col1, col2 = st.columns(2)
with col1:
    with st.expander("📅 Days 1–3: Diagnostic Setup & Ice-Breaking", expanded=True):
        st.markdown("**Day 1: Welcome & Document Hygiene Audit**")
        st.markdown("- **Action:** Program Manager provisions onboarding access to **Zoho Learn**. Collects academic transcripts from the past 3 years and passport details.")
        st.markdown("- <span class='pill-ops'>Ops Guardrail</span> Mandatory checklist check for transcripts; missing items trigger automated reminders within 24 hours.")
        
        st.markdown("**Day 2–3: Counselor Ice-Breaking & Psychometric Evaluation**")
        st.markdown("- **Action:** Primary counselor conducts a baseline discovery session. Student takes the online 45-minute psychometric assessment to map interests.")
        st.markdown("- <span class='pill-counselor'>Counselor Focus</span> Analyze natural alignment patterns (e.g., STEM, Business, Arts) ahead of the roadmap phase.")

with col2:
    with st.expander("📅 Days 4–7: ICP Alignment & Strategic Freeze", expanded=True):
        st.markdown("**Day 4–5: Profile Gap Generation & Target Filters**")
        st.markdown("- **Action:** Counselor uses psychometric data to build the initial **AS-IS vs. TO-BE Profile Gap Report** and establishes preliminary geographic/program targets.")
        
        st.markdown("**Day 6–7: The Master Roadmap Freeze**")
        st.markdown("- **Action:** Unified alignment session with parents and the student. Lock down subject mappings, standardized testing schedules, and milestone objectives.")
        st.markdown("- <span class='pill-value'>Admissions Value</span> Gives parents full visibility into the profile milestones needed to target top-tier universities.")

st.markdown("---")

# --- DATA GENERATOR FOR DYNAMIC GRADES ---
all_grades = ["Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"]
active_journey = all_grades[all_grades.index(selected_grade):]

st.markdown(f"## 🗺️ Your Tailored End-to-End Roadmap: From {selected_grade} to University Departure")

for grade in active_journey:
    st.markdown(f'<div class="grade-header">🏫 Full Execution Track: {grade}</div>', unsafe_allow_html=True)
    
    # ------------------ MIDDLE SCHOOL GENERATORS (GRADES 6-8) ------------------
    if grade in ["Grade 6", "Grade 7", "Grade 8"]:
        q_tabs = st.tabs(["🍂 Months 1–3 (Quarter 1)", "❄️ Months 4–6 (Quarter 2)", "🌱 Months 7–9 (Quarter 3)", "☀️ Months 10–12 (Summer Window)"])
        
        # GRADE 6
        if grade == "Grade 6":
            with q_tabs[0]:
                st.markdown('<div class="month-card"><strong>📋 Month 1–3 Focus: Core Academic Discipline & Habit Engineering</strong><br>'
                            '<div class="week-title">Week-on-Week Execution Log:</div>'
                            '• <b>Week 1-2:</b> Counselor runs a time-management audit to design a balanced weekly study schedule.<br>'
                            '• <b>Week 3-4:</b> Introduce basic analytical reading habits using targeted micro-assignments on Zoho Learn.<br>'
                            '• <b>Week 5-8:</b> Bi-weekly counselor checks to monitor school assignment turn-in rates and organization habits.<br>'
                            '• <b>Week 9-12:</b> First quarterly academic review. Identify areas needing academic support early.<br><br>'
                            '<span class="pill-counselor">Counselor Action</span> Instill positive study habits and track assignment completion data.<br>'
                            '<span class="pill-value">Admissions Value</span> Builds the GPA foundations necessary for advanced high school coursework.</div>', unsafe_allow_html=True)
            with q_tabs[1]:
                st.markdown('<div class="month-card"><strong>🎭 Month 4–6 Focus: Soft Skills & Communication Foundations</strong><br>'
                            '<div class="week-title">Week-on-Week Execution Log:</div>'
                            '• <b>Week 13-16:</b> Onboard student into basic public speaking exercises and speech structuring.<br>'
                            '• <b>Week 17-20:</b> Introduce low-stakes, constructive current events debate topics to practice basic research logic.<br>'
                            '• <b>Week 21-24:</b> Counselor evaluates reading logs and updates the student’s expanding vocabulary track.<br><br>'
                            '<span class="pill-counselor">Counselor Action</span> Lead speech drills and evaluate communicative confidence.<br>'
                            '<span class="pill-value">Admissions Value</span> Develops interview presence and clear communication early.</div>', unsafe_allow_html=True)
            with q_tabs[2]:
                st.markdown('<div class="month-card"><strong>🎨 Month 7–9 Focus: Cocurricular Exploration</strong><br>'
                            '<div class="week-title">Week-on-Week Execution Log:</div>'
                            '• <b>Week 25-28:</b> Audit school club choices. Guide the student to join 2 distinct, non-academic interest groups.<br>'
                            '• <b>Week 29-32:</b> Encourage participation in creative arts, sports, or music to see where natural dedication lies.<br>'
                            '• <b>Week 33-36:</b> Assist student in planning entry-level roles for upcoming middle school events or fests.<br><br>'
                            '<span class="pill-ops">Ops Guardrail</span> Verify that active certificates are added to the student dashboard at the close of Month 9.</div>', unsafe_allow_html=True)
            with q_tabs[3]:
                st.markdown('<div class="month-card"><strong>☀️ Month 10–12 Focus: Creative Summer Immersion</strong><br>'
                            '<div class="week-title">Week-on-Week Execution Log:</div>'
                            '• <b>Week 37-40:</b> Finalize enrollment in creative writing camps or beginner logic/coding bootcamps.<br>'
                            '• <b>Week 41-44:</b> Track execution of the summer project. Review reading logs via weekly checks.<br>'
                            '• <b>Week 45-48:</b> Run a comprehensive year-end parent review meeting to document growth and map Grade 7 transitions.<br><br>'
                            '<span class="pill-value">Admissions Value</span> Prevents summer learning loss and helps uncover organic creative interests.</div>', unsafe_allow_html=True)

        # GRADE 7
        elif grade == "Grade 7":
            with q_tabs[0]:
                st.markdown('<div class="month-card"><strong>🏆 Month 1–3 Focus: External Benchmarking & Competitive Sowing</strong><br>'
                            '<div class="week-title">Week-on-Week Execution Log:</div>'
                            '• <b>Week 1-4:</b> Select appropriate competitive examinations (Olympiads, ASSET) aligned with student academic strengths.<br>'
                            '• <b>Week 5-8:</b> Create a micro-study schedule using past diagnostic papers to build core testing confidence.<br>'
                            '• <b>Week 9-12:</b> Execute targeted preparation milestones. Run the first formal Grade 7 parent progress call.<br><br>'
                            '<span class="pill-counselor">Counselor Action</span> Review diagnostic performance and provide targeted practice metrics.<br>'
                            '<span class="pill-value">Admissions Value</span> Establishes an early academic track record outside of standard school grades.</div>', unsafe_allow_html=True)
            with q_tabs[1]:
                st.markdown('<div class="month-card"><strong>🚨 Month 4–6 Focus: Core Immigration Hygiene & Civil Responsibility</strong><br>'
                            '<div class="week-title">Week-on-Week Execution Log:</div>'
                            '• <b>Week 13-16:</b> <b>MANDATORY PASSPORT AUDIT:</b> Counselor reviews passport validity. If expired or unissued, trigger application workflows.<br>'
                            '• <b>Week 17-20:</b> Design a community service project (e.g., neighborhood collection drives or community center volunteering).<br>'
                            '• <b>Week 21-24:</b> Set up the community project timeline and begin tracking weekly engagement hours.<br><br>'
                            '<span class="pill-ops">Ops Guardrail</span> Passport verification flag must be resolved in the system by Week 16.<br>'
                            '<span class="pill-value">Admissions Value</span> Establishes a long-term commitment to community service, which is highly valued by top admissions boards.</div>', unsafe_allow_html=True)
            with q_tabs[2]:
                st.markdown('<div class="month-card"><strong>📚 Month 7–9 Focus: Advanced Analytical Literacy</strong><br>'
                            '<div class="week-title">Week-on-Week Execution Log:</div>'
                            '• <b>Week 25-28:</b> Introduce complex, curated reading materials (e.g., scientific journals, historical essays) via customized reading lists.<br>'
                            '• <b>Week 29-32:</b> Counselor runs 1:1 text analysis reviews to build critical thinking and textual comprehension skill sets.<br>'
                            '• <b>Week 33-36:</b> Student submits a 500-word book review analyzing themes, style, and personal conclusions.<br><br>'
                            '<span class="pill-counselor">Counselor Action</span> Review reading journals and guide thematic analysis discussions.</div>', unsafe_allow_html=True)
            with q_tabs[3]:
                st.markdown('<div class="month-card"><strong>☀️ Month 10–12 Focus: Design Thinking Workshops</strong><br>'
                            '<div class="week-title">Week-on-Week Execution Log:</div>'
                            '• <b>Week 37-40:</b> Student joins a structured 2-week design thinking and problem-solving workshop track.<br>'
                            '• <b>Week 41-44:</b> Document project outcomes (e.g., product prototypes or service solutions) into a visual project file.<br>'
                            '• <b>Week 45-48:</b> Run comprehensive document hygiene checks. Ensure all Grade 7 participation proofs are logged into CRM.<br><br>'
                            '<span class="pill-value">Admissions Value</span> Shifts student learning from passive intake to active, real-world application.</div>', unsafe_allow_html=True)

        # GRADE 8
        elif grade == "Grade 8":
            with q_tabs[0]:
                st.markdown('<div class="month-card"><strong>🧬 Month 1–3 Focus: High School Curriculum Strategy & Board Selection</strong><br>'
                            '<div class="week-title">Week-on-Week Execution Log:</div>'
                            '• <b>Week 1-4:</b> Analyze school board preferences (IB DP, AP pathways, Cambridge A-Levels, vs. National Boards) against geography targets.<br>'
                            '• <b>Week 5-8:</b> Map advanced high school subject criteria needed for target competitive courses (e.g., Engineering, Medicine, Economics).<br>'
                            '• <b>Week 9-12:</b> Finalize specific high school board recommendations and secure formal parent confirmation.<br><br>'
                            '<span class="pill-counselor">Counselor Action</span> Run curriculum comparison analytics meetings with the family.<br>'
                            '<span class="pill-value">Admissions Value</span> Avoids subject alignment gaps before entering high school transcripts.</div>', unsafe_allow_html=True)
            with q_tabs[1]:
                st.markdown('<div class="month-card"><strong>🔬 Month 4–6 Focus: Foundational Research Methodologies</strong><br>'
                            '<div class="week-title">Week-on-Week Execution Log:</div>'
                            '• <b>Week 13-16:</b> <b>Week 3 Batch Placement:</b> Transition student into the 3-month Uppseekers Foundational Research Cohort.<br>'
                            '• <b>Week 17-20:</b> Master basic source discovery, academic citation (APA/MLA frameworks), and information analysis methods.<br>'
                            '• <b>Week 21-24:</b> Select an exploratory research topic and write a structural outline under counselor review.<br><br>'
                            '<span class="pill-ops">Ops Guardrail</span> Track cohort session attendance weekly; report missing check-ins immediately.</div>', unsafe_allow_html=True)
            with q_tabs[2]:
                st.markdown('<div class="month-card"><strong>✍️ Month 7–9 Focus: Whitepaper Drafting & Execution</strong><br>'
                            '<div class="week-title">Week-on-Week Execution Log:</div>'
                            '• <b>Week 25-28:</b> Draft the body of the introductory research paper, focusing on clear problem definitions.<br>'
                            '• <b>Week 29-32:</b> Integrate feedback from writing tutors to polish flow, sentence structure, and evidence integration.<br>'
                            '• <b>Week 33-36:</b> Finalize the research paper and prepare a 5-minute presentation summarizing key arguments.<br><br>'
                            '<span class="pill-value">Admissions Value</span> Demonstrates early academic initiative beyond standard grade expectations.</div>', unsafe_allow_html=True)
            with q_tabs[3]:
                st.markdown('<div class="month-card"><strong>🏢 Month 10–12 Focus: Micro-Job Shadowing & High School Bridge</strong><br>'
                            '<div class="week-title">Week-on-Week Execution Log:</div>'
                            '• <b>Week 37-40:</b> Execute a 1-week micro-shadowing project at an aligned local business or organization.<br>'
                            '• <b>Week 41-44:</b> Complete a reflection log documenting operational observations and potential career alignments.<br>'
                            '• <b>Week 45-48:</b> Run a comprehensive middle-to-high-school bridge review. Finalize the student resume structure.<br><br>'
                            '<span class="pill-counselor">Counselor Action</span> Guide the translation of project work into the baseline high school resume.</div>', unsafe_allow_html=True)

    # ------------------ HIGH SCHOOL GENERATORS (GRADES 9-12) ------------------
    else:
        h_tabs = st.tabs([
            "📚 Academics & Standardized Testing", 
            "🔬 Research, Internships & Activities", 
            "✍️ Essay Engine & LOR Strategy", 
            "💼 Applications, Finances & Visas"
        ])
        
        # GRADE 9
        if grade == "Grade 9":
            with h_tabs[0]:
                st.markdown('<div class="month-card"><strong>📈 Month-on-Month Academic Rigor & Testing Foundations</strong><br>'
                            '• <b>Months 1-3:</b> Finalize the 4-year academic course matrix. Target maximum GPA targets on internal unit assessments.<br>'
                            '• <b>Months 4-6:</b> Counselor evaluates report cards monthly to identify subject gaps and recommend targeted tutoring support.<br>'
                            '• <b>Months 7-9:</b> Focus on vocabulary development and advanced math fundamentals to prepare for future test criteria.<br>'
                            '• <b>Months 10-12:</b> Final GPA evaluation. Update the student’s academic trajectory tracker based on final report cards.<br><br>'
                            '<span class="pill-value">Admissions Value</span> High school transcripts start now. Every final grade impacts the cumulative application GPA.</div>', unsafe_allow_html=True)
            with h_tabs[1]:
                st.markdown('<div class="month-card"><strong>🧪 Core Research Cohort & Extracurricular Alignment</strong><br>'
                            '• <b>Months 1-3:</b> Identify the student\'s thematic narrative angle. Choose 3 core school clubs to target for future leadership tracks.<br>'
                            '• <b>Months 4-6:</b> Commit to weekly club tasks. Initiate an independent, community-focused initiative.<br>'
                            '• <b>Months 7-10:</b> <b>Research Batch Entry:</b> Join a 4-month structured research cohort to write a domain whitepaper.<br>'
                            '• <b>Months 11-12:</b> Finish the whitepaper, upload it to the dashboard, and present findings to the internal student cohort.<br><br>'
                            '<span class="pill-ops">Ops Guardrail</span> Verify that research deliverables and cohort review matrices are completed by Month 11.</div>', unsafe_allow_html=True)
            with h_tabs[2]:
                st.markdown('<div class="month-card"><strong>📝 The 150-Word Weekly Reflective Writing Habit</strong><br>'
                            '• <b>Every Single Week (Friday Deadline):</b> Student must log a 150-word reflection on their dashboard detailing a meaningful personal interaction, challenge, or achievement from that week.<br>'
                            '• <b>Month-on-Month Review:</b> Counselor reads and critiques these entries every 30 days to build raw essay material early.<br><br>'
                            '<span class="pill-counselor">Counselor Action</span> Provide developmental writing feedback on students\' weekly reflection logs.<br>'
                            '<span class="pill-value">Admissions Value</span> Collects organic, unforced personal narratives that form the foundation of compelling college essays.</div>', unsafe_allow_html=True)
            with h_tabs[3]:
                st.markdown('<div class="month-card"><strong>📁 Financial Mapping & Monthly Document Hygiene</strong><br>'
                            '• <b>Every 30 Days:</b> Student must upload all report cards, participation certificates, and project outcomes to maintain clean records.<br>'
                            '• <b>Months 4-6:</b> Parents fill out the confidential Financial Horizon Questionnaire to flag budget boundaries and merit scholarship targets.<br>'
                            '• <b>Months 10-12:</b> Comprehensive review of year-1 documents. Ensure all data fields are verified in the CRM system.</div>', unsafe_allow_html=True)

        # GRADE 10
        elif grade == "Grade 10":
            with h_tabs[0]:
                st.markdown('<div class="month-card"><strong>✏️ Diagnostic Testing & Board Exam Prioritization</strong><br>'
                            '• <b>Months 1-3:</b> Run diagnostic SAT, ACT, and IELTS examinations to establish a baseline performance level.<br>'
                            '• <b>Months 4-6:</b> Build a test-prep calendar mapping out self-study blocks, mock testing windows, and target score goals.<br>'
                            '• <b>Months 7-9:</b> Intense focus on school board exam preparation. Pause non-essential external activities.<br>'
                            '• <b>Months 10-12:</b> Board examination execution phase. Post-board recovery and re-alignment interview setup.<br><br>'
                            '<span class="pill-counselor">Counselor Action</span> Review mock testing scores to adjust study timelines as needed.</div>', unsafe_allow_html=True)
            with h_tabs[1]:
                st.markdown('<div class="month-card"><strong>🏢 Leadership Transitions & Summer Corporate Internships</strong><br>'
                            '• <b>Months 1-3:</b> Secure active officer or committee positions within selected school organizations.<br>'
                            '• <b>Months 4-6:</b> Enter national or regional competitions (e.g., Hackathons, MUNs, Business Pitch events) to gain external recognition.<br>'
                            '• <b>Months 7-9:</b> <b>Summer Internship Window:</b> Transition into the structured corporate internship cohort matching the student\'s interest track.<br>'
                            '• <b>Months 10-12:</b> Complete 2-4 weeks of real-world internship engagement. Upload supervisor verification documents and the supervisor LOR.<br><br>'
                            '<span class="pill-value">Admissions Value</span> Provides real-world corporate exposure that sets the student apart from purely academic applicants.</div>', unsafe_allow_html=True)
            with h_tabs[2]:
                st.markdown('<div class="month-card"><strong>✍️ Essay Material Selection & Continuous Writing Logs</strong><br>'
                            '• <b>Weekly Cadence:</b> Maintain the mandatory 150-word weekly reflection habit on the student portal.<br>'
                            '• <b>Months 4-6:</b> Counselor extracts specific anecdotes from the student\'s internship logs to develop future personal statement essay concepts.<br>'
                            '• <b>Months 10-12:</b> Run structural writing tutorials to transition the student from descriptive to analytical essay composition.</div>', unsafe_allow_html=True)
            with h_tabs[3]:
                st.markdown('<div class="month-card"><strong>🛂 Passport Auditing & Preliminary Immigration Mapping</strong><br>'
                            '• <b>Months 1-3:</b> **CRITICAL TRANSITION CHECK:** Re-verify passport validity (must extend past intended graduation dates).<br>'
                            '• <b>Months 4-6:</b> Map initial student visa requirements by country (e.g., US F-1, UK Student Visa rules) to flag potential eligibility gaps.<br>'
                            '• <b>Every 30 Days:</b> Upload internal report cards, competition awards, and verified corporate internship certificates.</div>', unsafe_allow_html=True)

        # GRADE 11
        elif grade == "Grade 11":
            with h_tabs[0]:
                st.markdown('<div class="month-card"><strong>🎯 Standardized Test Sittings & Predicted Grade Tracking</strong><br>'
                            '• <b>Months 1-3:</b> Complete the first official sitting of the SAT, ACT, and IELTS/TOEFL assessments.<br>'
                            '• <b>Months 4-6:</b> Evaluate initial official scores against target university requirements. Pinpoint exact sub-score vulnerabilities.<br>'
                            '• <b>Months 7-9:</b> Run targeted test remediation sprints. Take the second official testing attempt to secure final target scores.<br>'
                            '• <b>Months 10-12:</b> Review school-allocated predicted grade matrices. Address any downward trends immediately.<br><br>'
                            '<span class="pill-ops">Ops Guardrail</span> Test score verification data must be updated in the internal CRM by Month 9.</div>', unsafe_allow_html=True)
            with h_tabs[1]:
                st.markdown('<div class="month-card"><strong>🔬 Advanced Mentorship Research Papers & Signature Passion Projects</strong><br>'
                            '• <b>Months 1-3:</b> Pair 1:1 with an expert domain mentor based on profile interest maps.<br>'
                            '• <b>Months 4-6:</b> Formulate an independent research question. Begin data gathering, literature reviews, and drafting pipelines.<br>'
                            '• <b>Months 7-9:</b> Launch a signature **Passion Project** (e.g., establishing a functioning social venture or developing a software app).<br>'
                            '• <b>Months 10-12:</b> Finalize the advanced research paper. Target submissions to peer-reviewed high school journals or open publication platforms.<br><br>'
                            '<span class="pill-value">Admissions Value</span> Demonstrates advanced academic curiosity and publication capabilities, highly valued by top-tier universities.</div>', unsafe_allow_html=True)
            with h_tabs[2]:
                st.markdown('<div class="month-card"><strong>💡 Personal Statement Brainstorming & Teacher LOR Strategy</strong><br>'
                            '• <b>Months 1-3:</b> Transition the weekly 150-word journal entries into the formal Common App Personal Statement workshop track.<br>'
                            '• <b>Months 4-6:</b> Deconstruct, select, and outline 3 core personal essay topics under counselor guidance.<br>'
                            '• <b>Months 7-9:</b> Complete the initial drafting phase for the core Personal Statement. Establish Statement of Purpose (SOP) structures for UK/Canada applications.<br>'
                            '• <b>Months 10-12:</b> Formulate a teacher LOR strategy. Share customized Uppseekers Brag Sheets with chosen academic recommenders.<br><br>'
                            '<span class="pill-counselor">Counselor Action</span> Review essay structures and provide feedback on initial personal statement drafts.</div>', unsafe_allow_html=True)
            with h_tabs[3]:
                st.markdown('<div class="month-card"><strong>🗺️ University Shortlisting & Scholarship Evaluation</strong><br>'
                            '• <b>Months 1-3:</b> Compile a balanced list of 20 tentative universities categorized by Reach, Match, and Safety metrics.<br>'
                            '• <b>Months 4-6:</b> Cross-reference university lists with family financial parameters to flag institutional merit opportunities.<br>'
                            '• <b>Months 7-9:</b> Refine the list based on actual standardized test results and updated profile milestones.<br>'
                            '• <b>Every 30 Days:</b> Upload official Grade 11 transcripts, test score reports, and passion project metrics.</div>', unsafe_allow_html=True)

        # GRADE 12
        elif grade == "Grade 12":
            with h_tabs[0]:
                st.markdown('<div class="month-card"><strong>🎓 Final Transcript Security & Portal Metric Delivery</strong><br>'
                            '• <b>June – August:</b> Consolidate official school transcript packets from Grades 9, 10, and 11 into a verified application format.<br>'
                            '• <b>September – November:</b> Fulfill mid-year reporting requests from early application universities.<br>'
                            '• <b>December – January:</b> Monitor board exam preparation trackers alongside application deadlines.<br>'
                            '• <b>February – April:</b> Submit final semester updates and grade cards to active university portal systems.<br><br>'
                            '<span class="pill-ops">Ops Guardrail</span> Run verification checks on transcript packages before submitting them to university portals.</div>', unsafe_allow_html=True)
            with h_tabs[1]:
                st.markdown('<div class="month-card"><strong>📁 Activity List Optimization & Portfolio Assembly</strong><br>'
                            '• <b>June – August:</b> Format the student\'s top 10 activities to match strict Common App limits (Role, Org, 150-character summary).<br>'
                            '• <b>September – November:</b> Compile specialized portfolios (e.g., research supplements, GitHub links, design slide decks) for application enhancement.<br>'
                            '• <b>December – January:</b> Lock down additional extracurricular updates to use as follow-up letters for target institutions.</div>', unsafe_allow_html=True)
            with h_tabs[2]:
                st.markdown('<div class="month-card"><strong>🏃 The Essay Writing Marathon & LOR Tracking</strong><br>'
                            '• <b>June – August:</b> Review and finalize the main **Common App Personal Statement**. Draft custom **Supplemental Essays** for target schools.<br>'
                            '• <b>September – November:</b> Polish specific country requirements (e.g., UCAS Personal Statement, Canadian SOP entries). Verify teacher LOR uploads.<br>'
                            '• <b>December – January:</b> Draft regular decision supplemental essays. Maintain a strict verification workflow for all written submissions.<br><br>'
                            '<span class="pill-counselor">Counselor Action</span> Review and edit every essay draft to ensure a consistent, authentic voice.</div>', unsafe_allow_html=True)
            with h_tabs[3]:
                st.markdown('<div class="month-card"><strong>🚀 Application Submissions, Visa Engineering & Pre-Departure Closure</strong><br>'
                            '• <b>June – August:</b> Finalize the official university list and map out specific course combinations.<br>'
                            '• <b>September – November:</b> Hand-hold line-by-line application form entries. Submit **Early Action (EA) & Early Decision (ED)** applications.<br>'
                            '• <b>December – January:</b> Submit all remaining **Regular Decision (RD)** applications. Conduct realistic mock admission interviews.<br>'
                            '• <b>February – April:</b> Track application portals for updates. Evaluate acceptance letters and scholarship offers. Confirm enrollment by paying the deposit.<br>'
                            '• <b>May – September:</b> **Visa Engineering Phase:** Compile bank statements and affidavits. Conduct visa mock interviews. Run pre-departure briefings.<br>'
                            '• <b>Post-Departure (Day 7–15):</b> Complete post-arrival check-ins with the student and parents to successfully close the case file.<br><br>'
                            '<span class="pill-value">Admissions Value</span> Flawless execution across every application step to ensure high acceptance rates and seamless international transitions.</div>', unsafe_allow_html=True)

    st.markdown("---")

# --- CENTRALIZED OPERATIONAL CONTROL MATRIX ---
st.markdown("## 🛡️ Internal Quality Control & Operational Guardrails")
st.markdown("*How the Uppseekers management and operations team enforces accountability across all tiers.*")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 👥 Counselor Action Items")
    st.markdown("1. **Weekly Progress Sprints:** Host structured 45-minute meetings to check milestone status and clear roadblocks.")
    st.markdown("2. **Critique the Writing Habit:** Read and provide developmental feedback on the student's 150-word weekly reflection logs.")
    st.markdown("3. **Document Auditing:** Review all student-uploaded transcripts and certificates for accuracy before verifying them.")

with c2:
    st.markdown("### 👪 Parent Transparency Loops")
    st.markdown("1. **Monthly Progress Updates:** Host a monthly 30-minute meeting to review the timeline calendar and preview upcoming goals.")
    st.markdown("2. **Shared WhatsApp Group:** Keep a direct chat active with parents, the counselor, and the operations manager for quick coordination.")
    st.markdown("3. **Strategic Approval Freeze:** Require formal parent sign-off on key decisions like university shortlists and major profile pivots.")

with c3:
    st.markdown("### 📊 Operations Team Systems")
    st.markdown("1. **CRM Dashboard Monitoring:** Run automated weekly checks to track counselor touchpoints and log completed tasks.")
    st.markdown("2. **Red-Flag Intervention:** Trigger system-level alerts if a session or milestone is missed for more than 48 hours.")
    st.markdown("3. **Cohort Operations Management:** Coordinate student schedules and capacity across active **Research Batches** and **Internship Cohorts**.")
