import streamlit as st
import pandas as pd
import plotly.express as px
import graphviz

# Set the title of the app
st.title("Ruslan Todorov's DevOps Resume")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Professional Experience", "Education", "Certifications", "Key Skills", "Projects", "Live Demos"])

# Home Page
if page == "Home":
    st.header("Contact Information")
    st.write("**Address:** 9 Kapina Street, Sofia, Sofia City, Bulgaria, 1282")
    st.write("**Phone:** +359 885 249 229")
    st.write("**Email:** expertpcin@gmail.com / devops_systems@outlook.com")
    st.write("**LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/ruslan-todorov-1695224b)")
    st.write("**Portfolio:** [My Portfolio](https://ruslantodorov.com)")  # Add your portfolio link

    st.header("Summary")
    st.write("Results-driven Certified DevOps / Systems Engineer with 20+ years of experience in IT, Cyber Security, and Cloud/DevOps. Proven track record of optimizing system performance, scalability, and reliability in fast-paced environments. Skilled in designing, implementing, and maintaining high-performing infrastructure solutions through continuous integration, continuous deployment, and automation processes.")

# Professional Experience Page
elif page == "Professional Experience":
    st.header("Professional Experience")

    st.subheader("Owner and DevOps Specialist, Sky Soft Bulgaria (Jun 2013 - Present)")
    st.write("• Founded Sky Soft Bulgaria, offering B2B DevOps solutions and services to businesses worldwide.")
    st.write("• Led the company's technical operations, focusing on optimizing software development processes.")
    st.write("• Implemented CI/CD pipelines for automated testing and deployment, ensuring efficiency and reliability, resulting in a 20% increase in deployment speed.")
    st.write("• Managed infrastructure as code, enhancing scalability, consistency, and security for B2B clients.")
    st.write("• Monitored system performance, identified and resolved issues to maintain high-quality services.")
    st.write("• Increased deployment efficiency by 20% through automation and process improvements.")

    st.subheader("DevOps Engineer, Sky Soft Bulgaria (Jun 2023 - Apr 2024)")
    st.write("• Implemented CI/CD pipelines for seamless testing and deployment automation, resulting in a 20% reduction in deployment time.")
    st.write("• Collaborated with cross-functional teams to design and execute backup and disaster recovery strategies.")

    st.subheader("IT Infrastructure Systems Engineer, eFellows, Bulgaria (Jun 2023 - Apr 2024)")
    st.write("• Designed and deployed scalable IT infrastructures to support business operations.")
    st.write("• Managed system configurations, upgrades, and optimizations for optimal performance and industry standards compliance.")

    st.subheader("Systems Operations, Mentor Mate, Sofia, Bulgaria (Jun 2022 - Sep 2022)")
    st.write("• Managed Windows server infrastructure, implementing security best practices to safeguard corporate networks.")
    st.write("• Conducted regular system updates and troubleshooting for uninterrupted operations.")

    st.subheader("Corporate Accounts Manager, EVRISTA LTD., Sofia, Bulgaria (Jun 2020 - Jun 2022)")
    st.write("• Managed corporate accounts and provided excellent client support.")

    st.subheader("IT Consultant and Entrepreneur, Bulgaria (Jan 2001 - Jun 2022)")
    st.write("• Provided technology consulting and management services to various clients.")
    st.write("• Sold technology solutions and offered service management for electronic security systems.")

    st.subheader("Custom Software Developer, CISA Electronic Systems Bulgaria (2001 - May 2022)")
    st.write("• Developed customized software solutions for clients in the hospitality industry.")
    st.write("• Created applications using .Net to address specific business needs.")
    st.write("• Tested servers, websites, and applications for vulnerabilities, ensuring robust security.")

# Education Page
elif page == "Education":
    st.header("Education")
    st.write("**Postgraduate Degree in DevOps, Caltech (Apr 2023)**")
    st.write("Earned industry-recognized certifications in DevOps practices.")
    st.write("Participated in intensive workshops and training sessions to enhance skills in CI/CD, IaC, and monitoring tools.")
    st.write("**Bachelor’s degree in Automation, Information and Control, Technical University Sofia (Jan 1999 – Dec 2010)**")
    st.write("High degree in Engines with internal combustion, Cars and trucks.")

# Certifications Page
elif page == "Certifications":
    st.header("Certifications")
    st.subheader("Cloud Certifications")
    st.write("• (ISC)² Certified in Cybersecurity (CC) - Self-Paced Training (2023)")
    st.write("• AWS Certified DevOps Engineer - Professional (2023)")
    st.write("• Docker Certified Associate (2023)")
    st.write("• Puppet Professional (2023)")

    st.subheader("DevOps Tools Certifications")
    st.write("• [Linux Training - 16 Feb 2023](https://success.simplilearn.com/71676896)")
    st.write("• [Induction for PGP in DevOps - 22 Feb 2023](https://success.simplilearn.com/71676896)")
    st.write("• [Agile Scrum Foundation - 28 Feb 2023](https://success.simplilearn.com/71676896)")
    st.write("• [Programming Fundamental - 28 Feb 2023](https://success.simplilearn.com/71676896)")
    st.write("• [Docker with IBM - 28 Feb 2023](https://success.simplilearn.com/71676896)")
    st.write("• [Kubernetes with IBM - 02 Mar 2023](https://success.simplilearn.com/71676896)")
    st.write("• [PGCP-Agile Scrum Master(ASM®) - 03 Mar 2023](https://success.simplilearn.com/71676896)")
    st.write("• [Getting Started with DevOps - 03 Mar 2023](https://success.simplilearn.com/71676896)")
    st.write("• [PGP-Docker Certified Associate (DCA) Training - 25 Mar 2023](https://success.simplilearn.com/71676896)")
    st.write("• [PGCP-DevOps on AWS - 29 Mar 2023](https://success.simplilearn.com/71676896)")
    st.write("• [PGP-DevOps Certification Training - 31 Mar 2023](https://success.simplilearn.com/71676896)")
    st.write("• [PG DO - Configuration Management with Ansible and Terraform - 04 Apr 2023](https://success.simplilearn.com/71676896)")
    st.write("• [PG DO - Container Orchestration Using Kubernetes - 12 Apr 2023](https://success.simplilearn.com/71676896)")
    st.write("• [Caltech CTME DevOps Academic Master Class - 13 Apr 2023](https://success.simplilearn.com/71676896)")
    st.write("• [Data Science with Python](https://success.simplilearn.com/71676896)")

# Key Skills Page
elif page == "Key Skills":
    st.header("Key Skills")
    st.write("• Azure DevOps Services")
    st.write("• Amazon Web Services (AWS)")
    st.write("• Google Cloud Platform (GCP)")
    st.write("• Linux")
    st.write("• Windows Server")
    st.write("• Continuous Integration/Continuous Deployment (CI/CD) – Jenkins / Azure DevOps")
    st.write("• Infrastructure as Code (IaC) – Terraform, Bicep, Code Based")
    st.write("• Monitoring and Performance Tuning")
    st.write("• Kubernetes k8s native / managed")
    st.write("• Collaboration and Communication")

# Projects Page
elif page == "Projects":
    st.header("Projects")
    st.write("• [Jenkins-Architecture-AWS](https://github.com/skynetlab1/Jenkins-Architecture-AWS.git) - This project demonstrates the setup and configuration of Jenkins on AWS, focusing on CI/CD pipelines and automated deployment processes for a sample web application.")
    st.write("• [BicepIaC](https://github.com/skynetlab1/BicepIaC.git) - This project showcases the use of Bicep for Infrastructure as Code (IaC) to manage and deploy Azure resources efficiently, focusing on a real-world scenario (e.g., creating a virtual machine with specific configurations).")

    # Embed a YouTube video
    st.subheader("Project Demo Video")
    st.video("https://www.youtube.com/watch?v=example_video_id")

    # Visualize Jenkins CI/CD Pipeline Architecture
    st.subheader("Jenkins CI/CD Pipeline Architecture on AWS")
    graph = graphviz.Digraph()
    with graph.subgraph(name='cluster_0') as c:
        c.attr(label='Jenkins CI/CD Pipeline', color='lightblue')
        c.node('github-source', 'GitHub Source', shape='box')
        c.node('jenkins-server', 'Jenkins Server', shape='box')
        c.node('maven-build', 'Maven Build', shape='box')
        c.node('npm-build', 'NPM Build', shape='box')
        c.node('docker-build', 'Docker Build', shape='box')
        c.node('sonarqube', 'SonarQube', shape='box')
        c.node('integration-testing', 'Integration Testing', shape='box')
        c.node('unit-testing', 'Unit Testing', shape='box')
        c.node('prod-testing', 'Production Testing', shape='box')
        c.node('preprod-testing', 'Pre-Production Testing', shape='box')
        c.node('artifactory', 'Artifactory', shape='box')
        c.node('ecr', 'ECR', shape='box')
        c.node('ecs', 'ECS', shape='box')
        c.node('public-container', 'Public Container', shape='box')

        c.edges([
            ('github-source', 'jenkins-server'),
            ('jenkins-server', 'maven-build'),
            ('jenkins-server', 'npm-build'),
            ('jenkins-server', 'docker-build'),
            ('maven-build', 'sonarqube'),
            ('maven-build', 'integration-testing'),
            ('npm-build', 'unit-testing'),
            ('docker-build', 'preprod-testing'),
            ('docker-build', 'artifactory'),
            ('artifactory', 'ecr'),
            ('ecr', 'ecs'),
            ('ecs', 'prod-testing'),
            ('prod-testing', 'public-container')
        ])

    st.graphviz_chart(graph)

# Live Demos Page
elif page == "Live Demos":
    st.header("Live Demos")

    # Example: Interactive Chart
    st.subheader("CI/CD Pipeline Performance")
    data = {
        "Pipeline": ["Pipeline 1", "Pipeline 2", "Pipeline 3", "Pipeline 4"],
        "Build Time (min)": [10, 15, 12, 18],
        "Success Rate (%)": [95, 90, 92, 88]
    }
    df = pd.DataFrame(data)
    fig = px.bar(df, x="Pipeline", y="Build Time (min)", color="Success Rate (%)", barmode="group")
    st.plotly_chart(fig)

    # Example: Interactive Map (if relevant)
    st.subheader("Global Deployment Map")
    data = {
        "City": ["Sofia", "New York", "London", "Tokyo"],
        "Latitude": [42.6977, 40.7128, 51.5074, 35.6895],
        "Longitude": [23.3219, -74.0060, -0.1278, 139.6917],
        "Deployments": [10, 15, 12, 18]
    }
    df = pd.DataFrame(data)
    fig = px.scatter_geo(df, lat="Latitude", lon="Longitude", size="Deployments", text="City",
                         projection="natural earth")
    st.plotly_chart(fig)

    # Example: Static Performance Metrics
    st.subheader("Static System Performance Metrics")
    performance_metrics = {
        "CPU Usage": "70%",
        "Memory Usage": "60%",
        "Disk Usage": "50%",
        "Network Throughput": "100 Mbps"
    }
    for metric, value in performance_metrics.items():
        st.write(f"{metric}: {value}")

# Run the Streamlit app
if __name__ == "__main__":
    st.sidebar.title("About")
    st.sidebar.info("This app is created using Streamlit to demonstrate DevOps skills and experience.")


