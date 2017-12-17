# linkScrape ![Supported Python versions](https://img.shields.io/badge/python-2.7-blue.svg)
      linkScrape.py v 1.09012017
      Description: Enumerates employee names from LinkedIn.com 
      Created by: Nick Sanzotta / @beamr
      Contributors: Jacob Robles / @shellfail

      ***********************************************************************************************

***
Installation:

    git clone https://github.com/NickSanzotta/linkScrape.git
    cd linkScrape
    python linkScrape.py --help
    
    3rd Party Python libraries may be required:
    pip install beautifulsoup4
    pip install bs4
    pip install lxml

***
Caveats

    Does not utilize LinkedIn's API.(This is a pure Web Scraper)
    LinkedIn Account may be flagged or banned.
    LinkedIn.com account will need 10+ connections/profile strength to perform searches.
    (This is a rough estimate based on current feedback)
    Company search results have a monthly cap.
    Script still has some minor bugs when scraping some character sets.
***
TIPS
      
      1. Use quotes for companies with white space.
      
            # python linkScrape.py -c'Eastman Kodak Company' -r1

             linkScrape.py v B1.01152017
             Description: Enumerates employee names from LinkedIn.com 
             Created by: @beamr
             ***********************************************************************************************

             Company Name: Eastman Kodak Company
             Industry / Employees: Printing; 5001-10,000 employees
             LinkedIn CompanyID: 1515
             URL:https://www.linkedin.com/company/1515

   
      2. Companies that share similar names, will produce multiple results and require the user to choose one.
         
             # python linkScrape.py -c'Eastman' -r1

             linkScrape.py v 1.01292017
             Description: Enumerates employee names from LinkedIn.com 
             Created by: @beamr
             ***********************************************************************************************

             1: Eastman Kodak Company
             2: Eastman Chemical Company
             3: Eastman
             4: Eastman Industrial Company
             5: Eastman Credit Union
            
              Please Select a Company: 1
              ENTERED: "Eastman Kodak Company"

              Company Name: Eastman Kodak Company
              Industry / Employees: Printing; 5001-10,000 employees
              LinkedIn CompanyID: 1515
              URL:https://www.linkedin.com/company/1515


 
***
Default Values:

    If a parameter is not defined it's default value will be choosen.
    Default values listed below.
  
    Mangle Option = 7  ex: FLast
    Page Results = 1-3
    Time out value = 3
    
***
Usage(CLI):

    Usage: python linkScrape.py <OPTIONS>
    Example[1]: python linkScrape.py -e LinkedInUser@email.com -c 'acme' -r 1-3 -t 3 -m 7 -d acme.com
    Example[2]: python linkScrape.py -e LinkedInUser@email.com -c 'acme' -r 3 -t 3 -m 7 -d acme.com
    Example[3]: python linkScrape.py -m 7 -i ~/Company/names.txt\n"
    Formatted output saved to: linkedIn/linkScrape-data/Company-mangle[x]_time.txt
    
    Login options:
    -e <email> Your LinkedIn.com Email Address.
    -p <pass>  Your LinkedIn.com Password. (If -p parameter is not defined, you'll be prompt to enter a password)
    
    Search options:
    -c <company> Company you want to enumerate.(Prepends to filename if used with -i) 
    -r <results> Searches X number of LinkedIn.com pages, or a range of pages (Default is 1-3).
    -t <secs>    Sets timeout value. (Default is 3.)
  ***
Mangle Options: 
    
    -m <mangle>
        1)FirstLast        
        2)LastFirst        
        3)First.Last       
        4)Last.First       
        5)First_Last       
        6)Last_First       
        7)FLast            
        8)LFirst           
        9)FirstL           
        10)F.Last          
        11)L.Firstname     
        12)FirLa           
        13)Lastfir
        14)FirstLastnam             
        15)LastF
        16)LasFi
        99)All              Mangle using all types

  
    -d <domain> Append @domain.com to enumerated user list."
    -i <input>  Use local file instead of LinkedIn.com to perform name Mangle."
    Misc:
    
    -h <help>  Prints this help menu.
  
 

***
Usage(Wizard):

      ENTERED: "acme"


       Mangle options:

             -m <mangle>		
                                       1)FirstLast        
                                       2)LastFirst        
                                       3)First.Last       
                                       4)Last.First       
                                       5)First_Last       
                                       6)Last_First       
                                       7)FLast            
                                       8)LFirst           
                                       9)FirstL           
                                      10)F.Last           
                                      11)L.Firstname      
                                      12)FirLa            
                                      13)Lastfir
                                      14)FirstLastnam
                                      15)LastF
                                      16)LasFi
                                      99)All              Mangle using all types

      Enter name Managle choice[ex:7]: 
      ENTERED: "7"

      [*]TIP: This value will determine how many page results will be returned.
      Enter number of pages results[ex:3] or a range of pages [ex:1-3]: 
      ENTERED: "1-3"

      [*]TIP: This value will determine how long of a delay(in seconds) each page will be scraped.
      Enter timeout value[ex:3]: 
      ENTERED: "3"

      [*]TIP: This value will be added to the end of each mangled result[ex:jsmith@acme.com].
      Enter Domain suffix[ex:acme.com]: acme.com
      ENTERED: "acme.com"



***
Output Sample:

       linkScrape.py v 1.01292017
       Description: Enumerates employee names from LinkedIn.com 
       Created by: @beamr
       ***********************************************************************************************

       1: ACME
       2: ACME
       3: ACME Cleantech Solution Private Limited
       4: Acme Markets
       5: Acme Packet

       Please Select a Company: 1
       ENTERED: "ACME"

       Company Name: ACME
       Industry / Employees: Design; 51-200 employees
       LinkedIn CompanyID: 139375
       URL:https://www.linkedin.com/company/139375


       Scraping Pages: 1-3


      Page: 1
      Ted Cullen : Director of
      Mary Gallagher : Human Resources
      Dan Carter : President at
      Suzy Alexander : VP of
      Conrad Burmester : Live Event
      Ashley Bryson : Fabrication Project
      Carol Lambert : Sales Development
      Mike Allen : VP of
      Matthew Castor : Senior Designer
      Frank Stenglein : Account Manager

      Page: 2
      Raena Mayhew : Manager of
      Marty Joyce : Senior Project
      Anja Taylor : Manager of
      Brooke Moerkerke : Purchasing Manager
      Melissa Esslemont : Marketing Coordinator
      michael von : Live Events
      Mark Bauch : Designer, Environmental
      Drew Flint : Production Manager
      Carla Solis : Project Manager

      Page: 3
      Bruce Farnsworth : Director at
      Kelli Strang : Project Manager
      Marc Tobia : Project Manager
      Worth (Ted : Project Manager
      Joseph Hewitt : IA 28
      brandon walter : Creative Technologist
      Dan Junor : Install Team
      Sabina Shaughnessy : Drafting Manager

       [*]Employee w/ Title list Saved to: linkScrape-data/acme_employee-title_20170124-0457.txt
       [*]Raw Employee list Saved to: linkScrape-data/acme_20170124-0457.txt
       [*]Mangled option chosen: 7
       [*]Mangled list Saved to: linkScrape-data/acme-mangle-7_20170124-0457.txt

      Completed in: 24.3s



