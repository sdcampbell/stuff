#!/usr/bin/env python2
# Description: Enumerates employee names from LinkedIn.com based off company search results.

import os, sys, getopt, getpass, json, re, requests, time
import argparse
from argparse import RawTextHelpFormatter
from sys import argv
from bs4 import BeautifulSoup
from pprint import pprint
from linkArguments import *
from linkMangle import *

curr_time = time.time()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def login(client, email, password):
    homepage = 'https://www.linkedin.com'
    login_page = 'https://www.linkedin.com/uas/login-submit'

    html = client.get(homepage).content
    soup = BeautifulSoup(html,'lxml')
    csrf = soup.find(id="loginCsrfParam-login")['value']
    login_information = {
        'session_key': email,
        'session_password': password,
        'loginCsrfParam': csrf,
        }

    login_response = client.post(login_page, data=login_information)

    # Validate Login.
    loginError = "Hmm, that's not the right password."
    if loginError in login_response.text:
        print(" Invalid Password.")
        print(" Exiting...")
        sys.exit(2)

#close the session created by the script
def logout():
    pass

#search for possible companies
def company_search(client,companyName,university):
    response = client.get('https://www.linkedin.com/ta/federator?orig=GLHD&verticalSelector=all&query='+companyName)
    json_string = json.loads(response.text)

    # Display the number of items in the JSON list "resultList"
    num_results = len(json_string['resultList'])

    # Create a new list for searched Companies
    companyList=[]
    for index in range(num_results):
        if not university:
            if 'company' in json_string['resultList'][index]['sourceID']:
                companyList.append(json_string['resultList'][index]['displayName'])
        else:
            if 'school' in json_string['resultList'][index]['sourceID']:
                companyList.append(json_string['resultList'][index]['displayName'])

    # Number of Companies now in companyList[]
    return companyList,json_string

#search employees based on company
def employee_search():
    pass

def connection(email, password, companyName, pageRange, timeout, university):
    #outputTitle value is only in the comments so far...
    #outputTitle = 'linkScrape-data/'+companyName+'_employee-title_'+timestr+'.txt'
    client = requests.Session()
    login(client, email, password)

    company_selected = False
    while not company_selected:
        #search for company
        companyList,json_string = company_search(client,companyName,university)
        num_companies = len(companyList)
        num_results = len(json_string['resultList'])

        index_select = False
        while not index_select:
            #print menu
            print(' ' + str(0) + ': Search again')
            for index in range(num_companies):
                print(' ' + str(index + 1) + ': ' + companyList[index])

            #get input, if not num, prompt again
            try:
                companyChoice = int(raw_input('\n Please Select a Company: '))
            except ValueError:
                continue 

            if companyChoice == 0:
                index_select = True
                companyName = raw_input('Enter Company[ex:acme]: ').strip()
            else:
                companyChoice=companyChoice-1
                #if valid, we can move on. else reprompt
                try:
                    print(' ENTERED: '+'"'+companyList[companyChoice]+'"')
                except IndexError:
                    continue

                companyName = companyList[companyChoice]
                index_select = True
                company_selected = True

    # Creates sublist for searched company with multiple results.
    subList=['']
    for index in range(num_results):
        # Checks for company/university name against list of results.
        # If name discovered, adds Industry/Empoyees/CompanyID/URL to subList.
        if not university:
            if companyName == json_string['resultList'][index]['displayName'] and \
                'company' in json_string['resultList'][index]['url']:
                subList.append(json_string['resultList'][index]['displayName'])
                subList.append(json_string['resultList'][index]['subLine'])
                subList.append(json_string['resultList'][index]['id'])
                subList.append(json_string['resultList'][index]['url'])
        else:
            if companyName == json_string['resultList'][index]['displayName'] and \
                'school' in json_string['resultList'][index]['url']:
                subList.append(json_string['resultList'][index]['displayName'])
                subList.append(json_string['resultList'][index]['subLine'])
                subList.append(json_string['resultList'][index]['id'])
                subList.append(json_string['resultList'][index]['url'])
    # Prints last 4 entries in the sublist.
    # The last entry in the sublist appears to always be correct
    # At least for now, will change if bugs are reported.
    print('\n Company Name: '+subList[-4]+'\n Industry / Employees: '\
            +subList[-3]+'\n LinkedIn CompanyID: '+subList[-2]+'\n URL:'+subList[-1])
    companyID = subList[-2]
    companyName = subList[-4]
    output = 'linkScrape-data/' + companyName + '_' + timestr + '.txt'
    outputTitle = 'linkScrape-data/'+companyName+'_employee-title_'+timestr+'.txt'

# HTML/SOUP PARSE

    # Define Page Range
    if not '-' in pageRange:
        pageStart = 1 
        pageEnd = int(pageRange)
    elif '-' in pageRange:
        page = pageRange.split('-')
        pageStart = page[0]
        pageEnd = page[1]
    else:
        print(' Please enter a valid integer or range: ')
        sys.exit(2)

    print(' Scraping Pages: '+ str(pageStart) + '-' + str(pageEnd) + '\n')
    
    # Defined a counter for corresponding page number
    # pageNumber variable is just for printing purposes...
    pageNumber = int(pageStart)-1

    #building URL based on company or school search
    url = 'https://www.linkedin.com/search/results/people/?'
    if not university:
        url += 'facetCurrentCompany=["' + companyID + '"]'
    else:
        url += '&facetSchool=["' + companyID + '"]&origin=FACETED_SEARCH'
    url += '&page='

    
    for index in range(int(pageStart),int(pageEnd)+1):
        time.sleep(timeout)
        response2 = client.get(url + str(index))
        #DEBUG: PRINT FULL HTLM PAGE
        # print(response2.text)
        # print('\n')
        
        soup = BeautifulSoup(response2.text,"lxml")
        prettySoup = soup.prettify().encode('utf-8')
        #DEBUG: PRINT FULL SOUP PAGE
        #print(soup.prettify().encode('utf-8'))
        #with open('tmp.txt', 'a') as tmp:
        #    tmp.write(soup.prettify().encode('utf-8'))
        # print('\n')
        
        #Parse Employee Names
        pageNumber+=1
        print('\nPage: ' + str(pageNumber))

        m1 = soup.find_all('code')
        m2 = re.findall(r'pdfFileName\=([\w]*)Profile', prettySoup)

        for line in m1:
            #datalet is not the droid we're looking for
            if 'datalet' not in line.get('id'):
                #print line.string
                #data we want is json formatted :)
                try:
                    pjson = json.loads(line.string)
                except ValueError:
                    continue
                for di in pjson['included']:
                    #we only care about dictionaries w/ first/last/occ
                    try:
                        firstName = di['firstName'].strip().encode('utf-8')
                        lastName = di['lastName'].strip().encode('utf-8')
                        occupation = di['occupation'].strip().encode('utf-8')
                    except KeyError:
                        continue
                    #cross ref with regex search
                    #if firstName+lastName not in m2:
                    #    continue
                    print firstName, lastName, ':', occupation
                    employee = firstName + ' ' + lastName
                    try:
                        employee = employee.encode('utf-8')
                    except UnicodeDecodeError:
                        continue
                    with open(output, 'a') as f:
                        f.write(employee + '\n')
                    with open(outputTitle, 'a') as f:
                        f.write(employee + ' : ' + occupation + '\n')
                #print json.dumps(pjson, indent=4, sort_keys=True)

    if not os.path.isfile(output):
        print(" No employees parsed...")
        print(" Exiting...")
        sys.exit(2)

    print(" [*]Raw Employee list Saved to: " + output)
    print(" [*]Employee w/ Title list Saved to: " + outputTitle)

    return companyName,output

def name(companyName, output, formatValue, domain):
    filename = "linkScrape-data/"+companyName+"-"+"mangle-"+str(formatValue)+"_"+timestr+".txt"

    if not os.path.isfile(output):
        print(" File not found...")
        print(" Exiting...")
        sys.exit(2)

    for x in open(output, 'r'):
        full_name = ''.join([c for c in x if  c == " " or  c.isalpha()])
        full_name = full_name.lower().split()
        first_name = full_name[0]
        last_name = full_name[-1]

        if formatValue == 1:
            newname = mangleOne(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 2:
            newname = mangleTwo(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 3:
            newname = mangleThree(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 4:
            newname = mangleFour(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 5:
            newname = mangleFive(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 6:
            newname = mangleSix(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 7:
            newname = mangleSeven(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 8:
            newname = mangleEight(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 9:
            newname = mangleNine(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 10:
            newname = mangleTen(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 11:
            newname = mangleEleven(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 12:
            newname = mangleTwelve(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 13:
            newname = mangleThirteen(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 14:
            newname = mangleFourteen(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 15:
            newname = mangleFifteen(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 16:
            newname = mangleSixteen(first_name, last_name, companyName, formatValue, domain, filename)
            # print(newname)
        elif formatValue == 99:
            mangleAll(first_name, last_name, companyName, formatValue, domain, filename)
        else:
            sys.exit(2)

    print(' [*]Mangled option chosen: '+ str(formatValue))
    print(' [*]Mangled list Saved to: '+filename)

if __name__ == "__main__":
    print(banner)
    args = parse_args()
    cls()
    print(banner)

    if not os.path.exists("linkScrape-data/"):
        os.mkdir("linkScrape-data/")
    if args.input:
        name(args.company, args.input, args.mangle, args.domain)
    else:
        company,output = connection(args.email, args.password, args.company, args.results, args.timeout, args.university)
        name(company, output, args.mangle, args.domain)
        print "\n Completed in: %.1fs\n" % (time.time() - curr_time)
