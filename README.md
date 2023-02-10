# py-bank
My second individual home assignment was to build a simple bank app using Jupyter Notebook making use of separate modules.

## Assignment (in Swedish)

I denna uppgift skall ni skapa objekten och funktionerna till en bank-applikation. Vi behöver inte kunna köra den som en applikation, men funktionerna skall finnas.

Skapa en ny sida i Jupyter Notebook. På denna sida skall ni skapa celler som skapar diverse objekt och funktioner. Skapa sedan objekt som innehåller denna information och kör sedan era funktioner. Användar-input är inte nödvändigt. Skriv ut så att man kan se att dina funktioner funkar.

Skapa en klass Account. Den skall ha kontonummer och saldo. Den bör ha en funktion för att ändra saldot med en summa, och en funktion för att hämta nuvarande saldot.

Skapa en klass Customer. Den skall ha användarnamn, lösenord och en lista av Accounts. En användare kan ha många konton. Den bör ha en funktion för att kolla om ett inskickat lösenord stämmer, samt en del funktioner som Bank använder sig av. Som add_account, som skall finnas i Bank, kanske skall finnas i Customer och användas.

Skapa en klass Bank. Den skall ha en lista av Customer, samt en variabel som skall innehålla kunden som just nu är inloggad. Vissa funktioner skall hända bara till kunden som just nu är inloggad.

Banken skall ha ett antal funktioner.

get_customers() – Lista alla kunder.

add_customer(name, password) – Lägg till en ny kund. Bör ta parametrar.

get_customer(name) – Hämta en specifik kund via användarnamn.

change_customer_password(name, new_password) – Ändra en kunds lösenord.

remove_customer(name) – Ta bort en kund.

login(name, password) – Om lösenordet stämmer, lägg till denna kunden från listan av kunder som vår nya inloggade kund.

logout() – Ta bort nuvarande användare från inloggade variabeln.

get_accounts() – Hämta alla konton som tillhör användaren som just nu är inloggad.

add_account(account_number) – Lägg till ett konto till kunden som just nu är inloggad.

remove_account(account_number) –Ta bort ett konto från kunden som just nu är inloggad.

get_account(account_number) – Hämtar ett konto från användaren som just nu är inloggad.

deposit(account_number, amount) – Lägg till pengar till ett konto som användaren har.

withdraw(account_number, amount) – Ta ut pengar från ett konto som användaren har.

Se till att alla dessa funktioner finns och de gör det som de skall. Funktioner som inte ger tillbaka objekt, till exempel change_customer_password, skall ge tillbaka True eller False beroende på om de lyckades eller inte. Kan inte ändra lösenord på en användare som inte finns. Om det inte finns ett objekt med namnet/numret som söks, till exempel man försöker göra get_account på ett nummer som inte finns, då skall den ge tillbaka None.

Använd dessa funktioner i separata celler och skriv ut relevant information för att vi skall se att det funkade. Hämtar ni pengar så skriv ut hur mycket pengar finns i kontot före och efter, etc.

För VG vill jag även att ni har gjort så att alla användarna och deras konton sparas i en text-fil. En användare per rad.

Exempel:

niklas/niklasPassword#konto1/321@konto2/500@konto3/261 james/jamesPassword#jamesKonto/-20 I ovan exempel så finns två användare, då det finns två rader. Informationen till vänster om # är användaren, användarnamn och lösenord avdelat med /. Informationen till höger om # är de olika konton användaren har. Dessa avskils av @. För varje konto så finns kontonummer/saldo. I början av programmet så kan du läsa in en textfil så att den skapar användare baserat på innehållet i filen, och skriv ut detta. Sedan skapa en egen sådan fil i slutet av programmet.

Utöver detta vill jag att ni har skapat separata moduler med de olika objekten och importerar dessa.

## ASSESSMENT (in Swedish)
Bedömning sker med följande betygskriterier

### För Godkänt (G) på arbetet skall följande krav uppfyllas:
* Skapa en Python Notebook sida som implementerar och använder sig av funktionerna listade i ”Vad skall ni göra?” sektionen, samt de objekt som beskrivs där.

### För Väl Godkänt (VG) på arbetet skall följande krav uppfyllas:
* Gör så att era objekt är i separata .py filer som laddas in av ert program.
* Gör även så att ni läser in användare från en tillhörande txt-fil (eller json-fil), och efter att ni gjort ändringar i programmet så sparar ni över den filen som fanns med den information som just nu finns i ert program.
