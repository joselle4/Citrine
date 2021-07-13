--------------------------------------------------------------      
**Title:** Citrine Informatics Code Challenge: GDB-17 Data Base     
                                                                    
**Author:** Joselle Abagat Barnett                                  
                                                                    
**Created Date:** July 9, 2019                                      
                                                                    
**Updated:** July 21, 2019                                          
                                                                    
--------------------------------------------------------------      

### Disclaimer:
This detailed project plan assumes certain roles, data sources, environments, etc.
Time line provides Project approach
--------------------------------------------------------------      
 
### Project Plan:
X-Materials has a few main goals for first year of their contract:

- Bring their data onto a centralized platform allowing for easy upload, access and storage of their data
- Organize their data in an intelligent and meaningful way
    - This organization should include the necessary context in order to enable a researcher to look up an experiment and understand the entire data related history of that experiment

--------------------------------------------------------------      
### Objective(s):
Bring X-Materials data onto a centralized data platform

--------------------------------------------------------------      
### Proposed Scope:
- Easy data upload, access and storage
- Organize data intelligently and meaningfully = Data modeling
- Provide experiment information: data and history
- Data conversion to CI Schema (PIF)
- Data load frequency

--------------------------------------------------------------      
## Interactions with the Customer
- contains expectations and questions to ask
### Resources and Roles from X-Materials:
#### Project Manager/Implementor
    – Expected to be one of the main collaborators 
    - To provide information regarding scheduling meetings, 
    testing, ensuring we get the support we need, etc.
    - What are your main requirements?
    - What do you consider out-of scope for this project?
#### Database Administrator (DBA) 
    – Expected to be the subject matter expert on database information
    - What is your data environment: RDBs vs Data Cubes vs NRDBs, etc.? 
    - What types of data access are we going to be provided with?
    - What is your data storage?
    - Can you provide us with your data schemas?
    - What are your data challenges?
        - Do you have unmodeled data?  
        If so, what can we do in order to assist with these data when going through 
        the data transformation and easy data upload to Citrine's platform?
        - What types of data hierarchies do you have?  What can 
        Citrine do to help develop needed data hierarchies?
    - What are your data onboarding challenges?
        - Do you have flat files that are not tabular?  If so, Citrine can assist 
        the best way to prepare this data for upload to the Citrine platform.
        - Do you have data that are not prepared consistently?  If so, Citrine can 
        support in developing templates in order to have consistency.
    - Do you have big data?
#### System Integration Analyst or Infrastructure Architect 
    - Expected to be the subject matter expert regarding data infrastructure:
        - Can you educate us on X-Materials' data infrastructure?
        - What are your different database integrations?
    - Are we going to have issues with going through your infrastructure for data access?
#### Data Analyst/Scientist
    – Expected to support with data investigation, prioritization, etc.
    - Which data needs to be prioritized first?
    - Do you have data in disparate sources or data that exists outside of your 
    existing databases?  If so, what can we do in order to support with the data being 
    loaded into the Citrine platform?
        - Preparing flat files?
        - Creating templates for tabularity?
        - Writing VBA code in order to manage Excel files?
    - Which of the data require hierarchies?  Can you provide us with the 
    hierarchy structure?
    - What customizations are needed to the data?
    - What are the data dependcies?
#### Material Developer/Researcher(s)
    - These should be researchers from at least a few business units 
    (like business units can provide the same representative) 
    – Should be a subject matter expert (SME)
    - SME to provide vision on how he/she foresees “experiment data and lookup”
#### Other End-User(s) 
    - These should be lead engineers from at least a few business units 
    (like business units can provide the same representative) 
    – should be a subject matter expert (SME)
    - SME to provide vision on how he/she foresees loading and accessing the data

--------------------------------------------------------------      
## Interactions within the Company
### Resources and Roles from CI:
#### Contract Manager/Buyer 
    – for contract definition/details
#### Front-End Developer 
    – to provide the following information GUI data model requirements
#### Data Scientist 
    - to provide the following information: 
        - ML data model requirements
#### Infrastructure Architect 
    – to provide support on:
        - Data infrastructure requirements
        - Data storage
        - Server requirements

--------------------------------------------------------------
### Summary of Challenges and Opportunities
#### Challenges:
    - Unmodeled data
    - Data hierarchy
    - Data in disparate sources or outside databases
    - Data access
    - Un-digitized data
#### Citrine can support with the following:
    - Creating data templates that can be uploaded easily
    - Creating VBA to manage Excel files
    - Guidance on preparing flat files
    - Discuss data governance 
    
--------------------------------------------------------------
### Time Line (provides approach to the project): 
#### Month 1
    - Meet with Resources from X-Materials and CI to finalize requirements, 
    ask questions, clarify data deliverables
    - Preliminary Data investigation:
        - Obtain list of database sources
            - Discuss how to access database sources, how to resolve access issues
            - For data cubes, discuss the best way to upload the data
        - Obtain list/collection of disparate data sources
            - Discuss guidelines on how to generate flat transfer files for disparate sources
            - Work on how to “prepare” the flat files for transfer
                - requires data to be prepared in a tabular format
                - for Excel files, provide some automation help using VBA if needed
#### Month 2
    - Data transfer/extract
        - Set-up database connections to AWS
        - Set-up data uploads to AWS
    - Data Investigation Deep Dive
        - Wrangle data
        - Identify data issues
        - Check for completeness
        - Start data structure/schema design
    - Bi-weekly meeting with customer
        - Discuss known data issues; ask about possible unknown data issues
        - Discuss data structure design
#### Month 3-6
    - Data modeling and transformation development
        - Continue data structure/schema design
        - Data history development
        - PIF Conversion
        - Identify data issues
        - Check for completeness
    - Bi-weekly meeting with customer
        - Continue data discussions
        - Discuss data development
        - Deliverables progress
#### Month 7-9
    - Data platform loading development
        - Design data platform development
        - Load data
        - Identify issues
        - Check for completeness
    - Monthly meeting with customer
        - Deliverables progress
#### Month 10
    - Customer test
    - Customer input/feedback
    - Data and Centralization Platform updates based on possible requirement changes or new requirements
    - Weekly meeting with customer
#### Month 11
    - Customer test
    - Customer input/feedback
    - Data and Centralization Platform updates based on possible requirement changes or new requirements
    - Weekly meeting with customer
#### Month 12
    - Finalize data centralization platform
    - Weekly meeting with customer
    - Transfer project to 2nd-year phase
 
 