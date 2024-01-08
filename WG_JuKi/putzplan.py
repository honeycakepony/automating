import csv
import os
from pathlib import Path
import datetime

NAMES = ['Ela', 'Gina', 'Hanna', 'Kathi', 'Lotte', 'Marius', 'Martin', 'Nico', 'Nina', 'Sarah', 'Unbekannt']
AUFGABEN = ['Esszimmer', 'Flur', 'Küche', 'Kühlschrank', 'Waschküche / Trockenraum / Dacia', 'Wohnzimmer']

def rotate(liste, start):
    result = list()
    for i in range(len(AUFGABEN)):
        print(start + i)
        pick = (start + i) % len(NAMES)
        result.append(liste[pick])
    return result


if __name__ == '__main__':
    assert len(NAMES) == 11, "Ein:e Bewohner:in zu wenig oder zu viel."
    assert len(AUFGABEN) == 6, "Eine Aufgabe zu wenig oder zu viel."

    alle_dienste = [rotate(NAMES, i * 5) for i in range(53)]

    counts = [0 for i in range(len(NAMES))]
    for sublist in alle_dienste:
        for elem in sublist:
            match elem:
                case 'Ela':
                    counts[0] += 1
                case 'Gina':
                    counts[1] += 1
                case 'Hanna':
                    counts[2] += 1
                case 'Kathi':
                    counts[3] += 1
                case 'Lotte':
                    counts[4] += 1
                case 'Marius':
                    counts[5] += 1
                case 'Martin':
                    counts[6] += 1
                case 'Nico':
                    counts[7] += 1
                case 'Nina':
                    counts[8] += 1
                case 'Sarah':
                    counts[9] += 1
                case 'Unbekannt':
                    counts[10] += 1
                case other:
                    assert False, "Tippfehler bei Bewohner:in"

    output_file = os.path.join(Path.home(), 'Desktop', 'Dienstplan.csv')
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        field = ['Kalenderwoche', 'Esszimmer', 'Flur', 'Küche', 'Kühlschrank',
                 'Waschküche / Trockenraum / Dacia', 'Wohnzimmer']
        writer.writerow(field)

        kw = 1
        date_start = datetime.datetime(2024, 1, 1)
        date_end = datetime.datetime(2024, 1, 7)
        for sublist in alle_dienste:
            kw_string = 'KW: ' + str(kw).zfill(2) + ', ' + str(date_start.strftime('%d-%m-%Y')) + ' - ' + str(date_end.strftime('%d-%m-%Y'))
            writer.writerow([kw_string, sublist[0], sublist[1], sublist[2], sublist[3], sublist[4], sublist[5]])
            kw += 1
            date_start += datetime.timedelta(days=7)
            date_end += datetime.timedelta(days=7)

    print(counts)
    print(alle_dienste)