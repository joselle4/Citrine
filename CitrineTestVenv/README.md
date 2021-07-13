--------------------------------------------------------------
**Title:** Citrine Informatics Code Challenge: GDB-17 Data Base

**Author:** Joselle Abagat Barnett

**Created Date:** July 3, 2019

**Updated:** July 17, 2019

--------------------------------------------------------------
_Disclaimer (per Julia): I have been programming in R full time in the last few years.  Therefore, my Python is very (very) rusty.  Please take that into consideration._

--------------------------------------------------------------
## Task 1:
Please write an ingester to transform a Python pandas data frame into the PIF format.  

#### Notes on XYZ file system:
    - Data is stored in xyz file system
    - xyz files is one of the normed file formats in chemistry
    - "report molecular structures and properties obtained from 
    quantum chemistry calculations for the first 134k molecules 
    of the chemical universe GDB-17 data base"
    
#### File Structure
Line    | Content
-------:|---------
1       | number of atoms (n_a)
2       | scalar properties
3-n_a+2 | element type, (x,y,z) coordinates, Mulliken partial atomic charge (in e)
n_a+3   | harmonic vibrational frequencies (in cm^-1)
n_a+4   | SMILES strings from GDB-17 and from B3LYP relaxation
n_a+5   | InChI strings for Corina and B3LYP geometries

#### Data Links:
- file structure
    - [data format link] <https://www.nature.com/articles/sdata201422#t2>
- line 2 of xyz file contains molecular geometries and 
    properties 
    - [data format link] <https://www.nature.com/articles/sdata201422#t3>

#### Data Citations:
- Rupp, Matthias; Ramakrishnan, Raghunathan; Dral, Pavlo; Anatole von Lilienfeld, O. (2015): Data for 6095 constitutional isomers of C7H10O2. figshare. Dataset.
- Rupp, Matthias; Ramakrishnan, Raghunathan; Dral, Pavlo; Anatole von Lilienfeld, O. (2018): Data for 133885 GDB-9 molecules. figshare. Dataset.
- Rupp, Matthias; Ramakrishnan, Raghunathan; Anatole von Lilienfeld, O.; Dral, Pavlo (2017): Validation: Benchmark  B3LYP, G4MP2, G4, CBS-QB3 enthalpies of atomization.. figshare. Dataset.
- Rupp, Matthias; Ramakrishnan, Raghunathan; Anatole von Lilienfeld, O.; Dral, Pavlo (2017): Readme file: Data description for "Quantum chemistry structures and properties of 134 kilo molecules". figshare. Dataset.
- Rupp, Matthias; Ramakrishnan, Raghunathan; Dral, Pavlo; Anatole von Lilienfeld, O. (2017): Atomref: Reference thermochemical energies of H, C, N, O, F atoms.. figshare. Dataset.
- Rupp, Matthias; Ramakrishnan, Raghunathan; Dral, Pavlo; Anatole von Lilienfeld, O. (2017): Uncharacterized: List of 3054 molecules which failed the geometry consistency check. figshare. Dataset.

#### Notes on PIF package:
    - all classes in common, except for property, uses pio 
    as a parameter
    - property class parameters: value class, rcl class
    - in the value class, there is a .scalar method.  
    Store line 2 here as an array of scalar properties?
    - in the value class, there is a .matrices method
    - value class has units; 
        - add units?  
        - create dictionary "column_name":"unit"

#### Approach:
1. Store datafiles into temporary directory for ease of access.
2. Loop through data files.
    - number of atoms will tell us how many lines are in each file: 
    - total number of lines = n_a + 5
3. Store as data frame or data table.
    - needs several data frames since they seem to all have varying rows/cols; 
        - one for the atoms/coordinates/mulliken partial charge
        - one for the scalar properties 
        - one for vibrational frequencies
        - SMILES
        - InChI
    - relate all using a unique ID - "tag + identifier" in line 2 of each file
    - this is load.py
4. Use PIF package to impose classification on data frame.
    - merge like data frames
    - loop through row items and use column names to invoke pif class objects
        - line 2 of the file scalar properties are going to be properties of the chemical system
        - same with the last three lines of the file (vibrational freq, SMILES, InChI)
   - what to do with atoms, coordinates and Mulliken Charge?
        - match IDs and nest within first loop
        - make it a composition class?
        - add coordinates and Mulliken charge as additional properties of class Composition
5. Use pif.dump method to create the json pif file
6. Create a python test file to output the json file

#### CitrineTestVenv Package Contents:
- **data Directory**
    - contains data folders for:
        - 6095 constitutional isomers of C7H10O2
        - 133885 GDB-9 molecules
- **src Directory**
    - contains the following source codes:
        - load.py: loads files into data frames
        - ingest.py: converts data frames contents into pif objects
        - test.py: outputs pif objects into json file
        - test_output.json: resultant file from test.py

--------------------------------------------------------------
## Task 2:
Say we are engaging with a new customer, X-Materials.  X-materials has hundreds of researchers working on dozens of materials development projects.  We have signed a two year contract, the first year of which will be devoted to getting their data onto the Citrination platform.

X-Materials has a few main goals for first year of their contract:

Bring their data onto a centralized platform allowing for easy upload, access and storage of their data
Organize their data in an intelligent and meaningful way
This organization should include the necessary context in order to enable a researcher to look up an experiment and understand the entire data related history of that experiment
While the end objective is to provide a data platform (enabled by the above goals and objectives) that allows X-Materials to utilize the Citrination platform to build machine learning models to guide their materials development efforts, this is not in the scope of the data engineers responsibilities in the first year of the contract.

As the Data Engineer on the team, propose a detailed project plan describing how you would approach and execute on understanding, organizing and capturing their data, and the challenges therein in order to deliver the first year goals and objectives.  This includes identifying who to speak with, what type of questions to ask, examining their data environment and the data itself, how to prioritize their data, how to assess the difficulty of onboarding that data and what type of tooling would assist you in the process.

Please see the attached organization chart for X-Materials.  This is an arbitrary representation only intended to give an idea of the complexity of a large materials industry organization, and what the structure might look like.  There is no need to focus on the specifics of this chart (i.e. no need to reference specific units or people).

In your detailed project plan, please make sure to address the following:

The goals and objectives described above
The tasks and considerations that are required to achieve those goals
The timeline of these required tasks 

### Project Plan:
see ProjectPlan.md