import os

def student():
    studentloop=True
    while studentloop==True:
        print('---------------------------------------------------------------------------------')
        print('Du har valgt å registrere en ny student')
        print('---------------------------------------------------------------------------------')
        
        #Variabel til while-løkke og registrert student
        ny_student= True
        ikke_registrert = False

        #Variabel til å sjekke student
        registrer_student='yes'

        #Åpner tekstfil i append for å legge til innhold i fil
        studentfil=open('student.txt','a')

        #While-løkke der brukeren skal oppgi informasjon om student
        while ny_student==True:
            print('Vennligst oppgi informasjon om studenten du ønsker å registrere!')
            studentnr=input('Studentnummer: ')
            fornavn=input('Fornavn: ')
            etternavn=input('Etternavn: ')
            studium=input('Studium: ')

            (studentfil.close)

            #Åpner tekstfil i read for å lese innhold
            studentfil=open('student.txt','r')

            #Leser første linje i filen
            registrert=studentfil.readline()

            #Sjekker om studenten er registrert fra før 
            while registrert!='':
                registrert=registrert.rstrip('\n')
                if studentnr==registrert:
                    ikke_registrert=True
                    print('Studenten er allerede registrert. Informasjonen vil ikke bli lagret.')

                registrert=studentfil.readline()
                registrert=registrert.rstrip('\n')

            #Åpner tekstfil i append for å legge til innhold i filen
            (studentfil.close)
            studentfil=open('student.txt','a')

            #Legger til studentinformasjon i filen dersom det ikke er registrert fra før
            if ikke_registrert==False:
                studentfil.write(studentnr+'\n')
                studentfil.write(fornavn+'\n')
                studentfil.write(etternavn+'\n')
                studentfil.write(studium+'\n')
                
            #Lukker studentfil
            studentfil.close()

            #Spør brukeren om hen ønsker å registrere en ny student
            ny=input('Ønsker du å registrere en ny student? (ja/nei)')
            if ny=='nei':
                studentloop=False
                ny_student=False

def slette():
    sletteloop=True
    while sletteloop==True:
        funnet=False
        print('---------------------------------------------------------------------------------')
        print('Du har valgt å slette en student')
        print('---------------------------------------------------------------------------------')
        
        #Spør brukeren om hvilken student som skal slettes
        oppgi_student=input('Vennligst oppgi studentnummeret på studenten du ønsker å slette: ')

        #Åpner eksamensresultat-fil
        leser_karakter=open('eksamensresultat.txt','r')

        #Leser gjennom eksamensresultats filen
        emnekode=leser_karakter.readline()

        #Leser gjennom hele filen og sjekker om studentnummeret er registrert med karakter
        while emnekode!='':
            emnekode=emnekode.rstrip('\n')
            studentnummer=leser_karakter.readline().rstrip('\n')
            karakter=leser_karakter.readline().rstrip('\n')

            if studentnummer==oppgi_student:
                funnet=True 
            
            emnekode=leser_karakter.readline()

        #Lukker eksamensresultats filen
        leser_karakter.close()

        #Sjekker i studentfilen dersom studentnummeret finnes i eksamensfil
        if not funnet:
            #Åpner den midlertidige filen
            midlertidig=open('temp.txt','w')
            
            #Åpner studentfil
            studentfil=open('student.txt','r')

            student_funnet=False

            studentnummeret=studentfil.readline()   

            #Leser gjennom studentfilen
            while studentnummeret!='':
                studentnummeret=studentnummeret.rstrip('\n')
                fornavn=studentfil.readline().rstrip('\n')
                etternavn=studentfil.readline().rstrip('\n')
                studium=studentfil.readline().rstrip('\n')
                
                #Leser inn i den midlertidige filen
                if studentnummeret!=oppgi_student:
                    midlertidig.write(studentnummeret+'\n')
                    midlertidig.write(fornavn+'\n')
                    midlertidig.write(etternavn+'\n')
                    midlertidig.write(studium+'\n')
                
                else:
                    student_funnet=True

                studentnummeret=studentfil.readline()   
            
            #Lukker studentfil
            studentfil.close()
            #Lukk midlertidig fil
            midlertidig.close()

            #Slett den orginale student.txt fila
            os.remove('student.txt')
                
            #Lager nytt navn på den midlertidige fila
            os.rename('temp.txt','student.txt')
            
            #Bruker en if-test på å lese ut om studenten er slettet eller om den ikke finnes
            if student_funnet==True:
                print('Studenten er slettet')
            else:
                print('Studenten finnes ikke')
        
        else:
            print('Studenten har karakterer og kan derfor ikke slettes')

        #Spør brukeren om hen ønsker å slette en til student
        slette_flere=input('Ønsker du å slette en til student? (ja/nei) ')
        if slette_flere=='ja':
            sletteloop=True
        else:
            sletteloop=False

def eksamensresultat():
    #Beregningsvariabler
    eksamensloop=True
    funnet=False
    funnet2=False
    lese_flere=False

    while eksamensloop==True:
        studentopplysninger=[]
        emneinfo=[]
        eksamensresultat=[]
        print('Du har valgt å skrive ut eksamensresultater for en student')
        studentnummer=input('Vennligst oppgi studentnummeret på studenten du ønsker eksamensresultater for: ')
        print('---------------------------------------------------------------------------------')


        #Åpner eksamensresultat
        eksamensfil=open('eksamensresultat.txt','r')

        #Leser første linje i filen
        emnenavn=eksamensfil.readline()

        #Leser gjennom eksamensfil helt til den er tom
        while emnenavn!='':
            emnenavn=emnenavn.rstrip('\n')
            studentnr=eksamensfil.readline().rstrip('\n')
            karakter=eksamensfil.readline().rstrip('\n')

            #Lagrer emnenavn, studentnummer og karakter hvis studenten har resultater
            if studentnummer==studentnr:
                funnet2==True
                eksamensresultat+=[emnenavn]
                eksamensresultat+=[studentnr]
                eksamensresultat+=[karakter]
            
            emnenavn=eksamensfil.readline()

        #Lukker eksamensfil
        eksamensfil.close()

        #Åpner studentfil
        studentfil=open('student.txt','r')

        #Leser første linje i studentfil
        studentnummeret=studentfil.readline()

        #Leser gjennom studentfil helt til den er tom
        while studentnummeret!='':
            studentnummeret=studentnummeret.rstrip('\n')
            fornavn=studentfil.readline().rstrip('\n')
            etternavn=studentfil.readline().rstrip('\n')
            studium=studentfil.readline().rstrip('\n')

            #Legger inn studentopplysninger hvis studenten finnes i systemet
            if studentnummeret==studentnummer:
                funnet=True
                studentopplysninger+=[studentnummeret]
                studentopplysninger+=[fornavn]
                studentopplysninger+=[etternavn]
                studentopplysninger+=[studium]
                
            studentnummeret=studentfil.readline()

        #Lukker studentfil
        studentfil.close()

        #Åpner emnefil
        emnefil=open('emne.txt','r')

        #Leser første linje i emnefil
        emnekode=emnefil.readline()

        #Leser gjennom emnefilen helt til den er tom
        while emnekode!='':
            emnekode=emnekode.rstrip('\n')
            emnenavn=emnefil.readline().rstrip('\n')
            emneinfo+=[emnekode]
            emneinfo+=[emnenavn]
            
            emnekode=emnefil.readline()

        #Sjekker om studenten er funnet eller ikke
        if funnet==True and funnet2==True:
            print('Studentopplysninger:',studentopplysninger[0],studentopplysninger[1],studentopplysninger[2],studentopplysninger[3])
        else:
            print('Studenten har ikke karakterer eller er ikke registrert i systemet')

        #Bruker for-løkke for å finne riktig verdi på emnekode, karakter, emneinfo og emnenavn
        for n in range(0,len(eksamensresultat),3):
            emnekode=eksamensresultat[n]
            karakter=eksamensresultat[n+2]

            for m in range(0,len(emneinfo),2):
                if emneinfo[m]==emnekode:
                    emnenavn=emneinfo[m+1]

            print('Eksamensresultat i faget:',emnekode,emnenavn,'er karakteren',karakter)

        #Spør brukeren om det skal skrives ut eksamensresultater til flere studenter
        print('---------------------------------------------------------------------------------')
        lese_flere=input('Ønsker du å skrive ut eksamensresultat til en ny student? (ja/nei)')

        if lese_flere=='ja':
            eksamensloop=True
        else:
            eksamensloop=False

def main():
    mainloop=True
    while mainloop==True:
        print('---------------------------------------------------------------------------------')
        print('Meny')
        print('Valg 1 - legge til student')
        print('Valg 2 - slette student')
        print('Valg 3 - skriv ut karakterliste for studenten')
        print('Valg 9 - avslutt program')
        print('---------------------------------------------------------------------------------')
        valg=input('Hva vil du gjøre? ')
        print('---------------------------------------------------------------------------------')

        if valg=='1':
            student()

        if valg=='2':
            slette()

        if valg=='3':
            eksamensresultat()

        if valg=='9':
            mainloop=False
        
main()
