<?xml version="1.0" encoding="UTF-8"?>
<xliff version="1.2" xmlns="urn:oasis:names:tc:xliff:document:1.2" xmlns:okp="okapi-framework:xliff-extensions" xmlns:its="http://www.w3.org/2005/11/its" xmlns:itsxlf="http://www.w3.org/ns/its-xliff/" its:version="2.0">
<file original="hairdressers_en.md" source-language="en" target-language="fr" datatype="x-text/markdown" okp:inputEncoding="UTF-8">
<body>
<trans-unit id="tu1" xml:space="preserve">
<source xml:lang="en">Programming task Hairdressers</source>
<target xml:lang="fr">Programming task Hairdressers</target>
</trans-unit>
<trans-unit id="tu2" xml:space="preserve">
<source xml:lang="en"><g id="1">Memory limit</g>: 4 MiB<x id="2"/>
<g id="3">Time limit</g>: 0.2 second<x id="4"/>
<g id="5">Input file</g>: <g id="6">hair.in</g><x id="7"/>
<g id="8">Output</g>: <g id="9">hair.out</g></source>
<target xml:lang="fr"><g id="1">Memory limit</g>: 4 MiB<x id="2"/>
<g id="3">Time limit</g>: 0.2 second<x id="4"/>
<g id="5">Input file</g>: <g id="6">hair.in</g><x id="7"/>
<g id="8">Output</g>: <g id="9">hair.out</g></target>
</trans-unit>
<trans-unit id="tu3" xml:space="preserve">
<source xml:lang="en">Description</source>
<target xml:lang="fr">Description</target>
</trans-unit>
<trans-unit id="tu4" xml:space="preserve">
<source xml:lang="en">In a big city (more than one million of inhabitants, though no more than a billion) there is one and only one hair studio, with only a few hairdressers (their number is up to $9$). Each of the hairdressers has a unique number in $<g id="1">1..9</g>$, enabling a more efficient service. The studio measures the time in certain time units $<g id="2">1\,..\,2\,000\,000\,000</g>$, and time counting starts at the studio opening moment.</source>
<target xml:lang="fr">Vienaa lielaa pilseetaa(more than one million of inhabitants, though no more than a billion) there is one and only one hair studio, with only a few hairdressers (their number is up to $9$). Each of the hairdressers has a unique number in $<g id="1">1..9</g>$, enabling a more efficient service. The studio measures the time in certain time units $<g id="2">1\,..\,2\,000\,000\,000</g>$, and time counting starts at the studio opening moment.</target>
</trans-unit>
<trans-unit id="tu5" xml:space="preserve">
<source xml:lang="en">Even though the number of customers is huge and the demand for hairdressers is very high, every hairdresser should take mandatory breaks. The time of a mandatory break for each hairdresser is when the hundreds digit in the time number coincides with the hairdresser’s number. For example, the hairdresser with number $5$ has to take a break in the time intervals $<g id="1">500..599</g>$, $<g id="2">1500..1599</g>$, $<g id="3">2500..2599</g>$, etc. During a break, hairdresser is forbidden to serve a client. In addition, customer appointment cannot be divided in stages, i.e. customer can only be served by one hairdresser without any breaks. Consequently, a hairdresser cannot start to serve a client, if the service cannot be finished before the break starts.</source>
<target xml:lang="fr">Even though the number of customers is huge and the demand for hairdressers is very high, every hairdresser should take mandatory breaks. The time of a mandatory break for each hairdresser is when the hundreds digit in the time number coincides with the hairdresser’s number. For example, the hairdresser with number $5$ has to take a break in the time intervals $<g id="1">500..599</g>$, $<g id="2">1500..1599</g>$, $<g id="3">2500..2599</g>$, etc. During a break, hairdresser is forbidden to serve a client. In addition, customer appointment cannot be divided in stages, i.e. customer can only be served by one hairdresser without any breaks. Consequently, a hairdresser cannot start to serve a client, if the service cannot be finished before the break starts.</target>
</trans-unit>
<trans-unit id="tu6" xml:space="preserve">
<source xml:lang="en">A customer should be served without delay if there is an unoccupied hairdresser and she/he does not have any limitations regarding this work. Upon finishing work with the current client, a hairdresser should immediately try to start serving the next one. More precisely: a client $C_1$ shows up at the time moment $T_1$ and his appointment needs time (serving duration) $D_1$. The hairdresser $H_1$ is currently free. Consequently, this appointment will take place during time interval $<g id="1">T_1..T_1+D_1-1</g>$. The appointment is finished at the time moment $T_1+ D_1-1$. If a customer $C_2$ has already shown up before or exactly during time moment $T_1+D_1$, then hairdresser $H_1$ can start working with customer $C_2$ at the time moment $T_1+ D_1$.</source>
<target xml:lang="fr">A customer should be served without delay if there is an unoccupied hairdresser and she/he does not have any limitations regarding this work. Upon finishing work with the current client, a hairdresser should immediately try to start serving the next one. More precisely: a client $C_1$ shows up at the time moment $T_1$ and his appointment needs time (serving duration) $D_1$. The hairdresser $H_1$ is currently free. Consequently, this appointment will take place during time interval $<g id="1">T_1..T_1+D_1-1</g>$. The appointment is finished at the time moment $T_1+ D_1-1$. If a customer $C_2$ has already shown up before or exactly during time moment $T_1+D_1$, then hairdresser $H_1$ can start working with customer $C_2$ at the time moment $T_1+ D_1$.</target>
</trans-unit>
<trans-unit id="tu7" xml:space="preserve">
<source xml:lang="en">Clients wait in a queue, they are admitted strictly on the first come first served basis. If the first client in the queue cannot be served
(his duration exceeds the remaining time until the breaks of all hairdressers who are currently free), then everyone in the queue waits.
At any time moment, no more than one customer can show up.
Administrator immediately assigns a number in queue $<g id="1">1\,..\,200\,000</g>$ and an appointment duration $<g id="2">1..900</g>$.</source>
<target xml:lang="fr">Clients wait in a queue, they are admitted strictly on the first come first served basis. If the first client in the queue cannot be served
(his duration exceeds the remaining time until the breaks of all hairdressers who are currently free), then everyone in the queue waits.
At any time moment, no more than one customer can show up.
Administrator immediately assigns a number in queue $<g id="1">1\,..\,200\,000</g>$ and an appointment duration $<g id="2">1..900</g>$.</target>
</trans-unit>
<trans-unit id="tu8" xml:space="preserve">
<source xml:lang="en">If there is an unserved customer and there are multiple hairdressers that lay claim on her, then:</source>
<target xml:lang="fr">If there is an unserved customer and there are multiple hairdressers that lay claim on her, then:</target>
</trans-unit>
<trans-unit id="tu9" xml:space="preserve">
<source xml:lang="en">The hairdresser that has spent more time without a customer (counting from the end of the last appointment), has the priority;</source>
<target xml:lang="fr">The hairdresser that has spent more time without a customer (counting from the end of the last appointment), has the priority;</target>
</trans-unit>
<trans-unit id="tu10" xml:space="preserve">
<source xml:lang="en">If two hairdressers have spent the same time without a client, the hairdresser with the smaller number has the priority.</source>
<target xml:lang="fr">If two hairdressers have spent the same time without a client, the hairdresser with the smaller number has the priority.</target>
</trans-unit>
<trans-unit id="tu11" xml:space="preserve">
<source xml:lang="en">Knowing the times, when customers show up, their numbers in the queue, the durations of the appointments, our task is to print the appointment end time for each customer, as well as the number of serving hairdresser and the customer's number in the queue. The records should be in ascending order by the appointment finishing time. If two client appointments were finished at the same time, results should be ordered by the hairdresser number.</source>
<target xml:lang="fr">Knowing the times, when customers show up, their numbers in the queue, the durations of the appointments, our task is to print the appointment end time for each customer, as well as the number of serving hairdresser and the customer's number in the queue. The records should be in ascending order by the appointment finishing time. If two client appointments were finished at the same time, results should be ordered by the hairdresser number.</target>
</trans-unit>
<trans-unit id="tu12" xml:space="preserve">
<source xml:lang="en">Input:</source>
<target xml:lang="fr">Input:</target>
</trans-unit>
<trans-unit id="tu13" xml:space="preserve">
<source xml:lang="en">The first line has the integer number that is the number of hairdressers. Then follows the information about the customers in the order of showing up (Ascending time values).</source>
<target xml:lang="fr">The first line has the integer number that is the number of hairdressers. Then follows the information about the customers in the order of showing up (Ascending time values).</target>
</trans-unit>
<trans-unit id="tu14" xml:space="preserve">
<source xml:lang="en">Hairdressers
Time Customer Duration
...
0
</source>
<target xml:lang="fr">Hairdressers
Time Customer Duration
...
0
</target>
</trans-unit>
<trans-unit id="tu15" xml:space="preserve">
<source xml:lang="en"><g id="1">Hairdressers</g> denotes the number of hairdressers $<g id="2">1..9</g>$</source>
<target xml:lang="fr"><g id="1">Hairdressers</g> denotes the number of hairdressers $<g id="2">1..9</g>$</target>
</trans-unit>
<trans-unit id="tu16" xml:space="preserve">
<source xml:lang="en"><g id="1">Time</g> denotes the moment in time, when customer has shown up and is ready to have an appointment $<g id="2">1\,..\,2\,000\,000\,000</g>$</source>
<target xml:lang="fr"><g id="1">Time</g> denotes the moment in time, when customer has shown up and is ready to have an appointment $<g id="2">1\,..\,2\,000\,000\,000</g>$</target>
</trans-unit>
<trans-unit id="tu17" xml:space="preserve">
<source xml:lang="en"><g id="1">Customer</g> denotes the customer number in the queue $<g id="2">1\,..\,200\,000</g>$</source>
<target xml:lang="fr"><g id="1">Customer</g> denotes the customer number in the queue $<g id="2">1\,..\,200\,000</g>$</target>
</trans-unit>
<trans-unit id="tu18" xml:space="preserve">
<source xml:lang="en"><g id="1">Duration</g> denotes the necessary length of the appointment $<g id="2">1..900</g>$</source>
<target xml:lang="fr"><g id="1">Duration</g> denotes the necessary length of the appointment $<g id="2">1..900</g>$</target>
</trans-unit>
<trans-unit id="tu19" xml:space="preserve">
<source xml:lang="en"><g id="1">0</g> means the end of input data. In this case, <g id="2">Customer</g> and <g id="3">Duration</g> fields are not provided</source>
<target xml:lang="fr"><g id="1">0</g> means the end of input data. In this case, <g id="2">Customer</g> and <g id="3">Duration</g> fields are not provided</target>
</trans-unit>
<trans-unit id="tu20" xml:space="preserve">
<source xml:lang="en">Input data is in ascending chronological order by <g id="1">Time</g>.</source>
<target xml:lang="fr">Input data is in ascending chronological order by <g id="1">Time</g>.</target>
</trans-unit>
<trans-unit id="tu21" xml:space="preserve">
<source xml:lang="en">The input file is correct regarding the input data format and the given conditions.</source>
<target xml:lang="fr">The input file is correct regarding the input data format and the given conditions.</target>
</trans-unit>
<trans-unit id="tu22" xml:space="preserve">
<source xml:lang="en">Output:</source>
<target xml:lang="fr">Output:</target>
</trans-unit>
<trans-unit id="tu23" xml:space="preserve">
<source xml:lang="en">According to the input file, each of the customer appointment end time is written in the following format:</source>
<target xml:lang="fr">According to the input file, each of the customer appointment end time is written in the following format:</target>
</trans-unit>
<trans-unit id="tu24" xml:space="preserve">
<source xml:lang="en">Time Hairdresser Customer
</source>
<target xml:lang="fr">Time Hairdresser Customer
</target>
</trans-unit>
<trans-unit id="tu25" xml:space="preserve">
<source xml:lang="en"><g id="1">Time</g> denotes the moment in time, which is the last customer appointment moment $<g id="2">1\,..\,2\,000\,000\,000</g>$.</source>
<target xml:lang="fr"><g id="1">Time</g> denotes the moment in time, which is the last customer appointment moment $<g id="2">1\,..\,2\,000\,000\,000</g>$.</target>
</trans-unit>
<trans-unit id="tu26" xml:space="preserve">
<source xml:lang="en"><g id="1">Hairdresser</g> denotes the hairdresser that served the customer, i.e. the hairdresser number $<g id="2">1..9</g>$.</source>
<target xml:lang="fr"><g id="1">Hairdresser</g> denotes the hairdresser that served the customer, i.e. the hairdresser number $<g id="2">1..9</g>$.</target>
</trans-unit>
<trans-unit id="tu27" xml:space="preserve">
<source xml:lang="en"><g id="1">Customer</g> denotes the customer that had the appointment - his/her number in queue $<g id="2">1\,..\,200\,000</g>$.</source>
<target xml:lang="fr"><g id="1">Customer</g> denotes the customer that had the appointment - his/her number in queue $<g id="2">1\,..\,200\,000</g>$.</target>
</trans-unit>
<trans-unit id="tu28" xml:space="preserve">
<source xml:lang="en">In the result, none of the appointment end time will not be greater than $2\,000\,000\,000$.</source>
<target xml:lang="fr">In the result, none of the appointment end time will not be greater than $2\,000\,000\,000$.</target>
</trans-unit>
<trans-unit id="tu29" xml:space="preserve">
<source xml:lang="en">Example:</source>
<target xml:lang="fr">Example:</target>
</trans-unit>
<trans-unit id="tu30" xml:space="preserve">
<source xml:lang="en">The content of input file <g id="1">hair.in</g>:</source>
<target xml:lang="fr">The content of input file <g id="1">hair.in</g>:</target>
</trans-unit>
<trans-unit id="tu31" xml:space="preserve">
<source xml:lang="en">2
11 1 10
21 2 50
31 3 20
0
</source>
<target xml:lang="fr">2
11 1 10
21 2 50
31 3 20
0
</target>
</trans-unit>
<trans-unit id="tu32" xml:space="preserve">
<source xml:lang="en">The content of output file <g id="1">hair.out</g>:</source>
<target xml:lang="fr">The content of output file <g id="1">hair.out</g>:</target>
</trans-unit>
<trans-unit id="tu33" xml:space="preserve">
<source xml:lang="en">20 1 1
50 1 3
70 2 2
</source>
<target xml:lang="fr">20 1 1
50 1 3
70 2 2
</target>
</trans-unit>
</body>
</file>
</xliff>
