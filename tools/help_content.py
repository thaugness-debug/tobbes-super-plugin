import sys, pathlib
root = pathlib.Path(sys.argv[1])
# (tittel, tekst) – tekst None = overskrift i lista
T = [
("GRUNNKURS", None),
("Hva gjør hva?", """OSC 1-3 er lydkildene. Hver av dem spiller en bølgeform. Skru LEVEL for volum og PITCH for å flytte den opp eller ned i halvtoner.

UNISON lager flere kopier av samme tone. Det første tallet er antall stemmer, prosenten er hvor mye de er stemt fra hverandre. Mange stemmer + litt detune = bred og feit lyd.

FILTER 1 og 2 fjerner deler av lyden. CUTOFF bestemmer hvor mye lyst som slipper gjennom, RESONANCE lager en topp akkurat der filteret kutter.

ENV 1 styrer volumet over tid: ATTACK (hvor fort lyden kommer), DECAY (hvor fort den faller), SUSTAIN (nivået mens du holder tasten) og RELEASE (hvor lenge den henger igjen).

ENV 2-3 og LFO 1-4 er bevegelse. Dra navnet (f.eks. LFO 1) og slipp det på en knott, så beveger knotten seg av seg selv.

EFFECTS-fanen er der lyden blir ferdig: distortion, kompressor, chorus, delay og reverb."""),
("Slik får du bevegelse", """1. Finn knotten du vil ha liv i, for eksempel CUTOFF på FILTER 1.
2. Dra ENV 2 eller LFO 1 fra høyre side og slipp på knotten.
3. En liten ring dukker opp ved knotten. Dra i den for å bestemme hvor mye den skal bevege seg.
4. ENV = én bevegelse hver gang du trykker en tast. LFO = bevegelse som gjentar seg i takt.
5. På LFO-en velger du hastighet under FREQUENCY (1/4, 1/8 osv. følger tempoet i FL).

Tips: MACRO 1-4 til venstre fungerer på samme måte. Dra en macro til flere knotter, så styrer du alle med én."""),
("LEADS", None),
("Supersaw-lead", """Den store, brede lyden fra progressive house.

1. OSC 1: la bølgeformen være sag (Init). UNISON: 7-9 stemmer, detune rundt 20-30 %.
2. Skru på OSC 2 med samme oppsett, men PITCH +12 (en oktav opp) og litt lavere LEVEL.
3. ENV 1: ATTACK helt ned, SUSTAIN høyt, RELEASE ca. 0,2-0,4 s.
4. FILTER 1 på (Analog 12dB), CUTOFF ganske åpent. Send OSC 1 og 2 til filteret.
5. EFFECTS: Chorus av, Reverb på med MIX rundt 20-30 %, Delay svakt.
6. Compressor på for å lime det sammen.

For tynn? Flere unison-stemmer. For grøtete? Mindre detune og mindre reverb."""),
("Pluck", """Kort, sprettende lyd til melodier og akkorder.

1. Start med en sag på OSC 1, UNISON 3-5 stemmer, lite detune.
2. FILTER 1 på, CUTOFF ganske lavt.
3. Dra ENV 2 til CUTOFF og skru mengden opp.
4. ENV 2: ATTACK 0, DECAY kort (0,1-0,3 s), SUSTAIN 0. Nå åpner filteret seg raskt og lukker seg igjen.
5. ENV 1: SUSTAIN lavt og RELEASE kort for en stram lyd.
6. Litt Delay og Reverb gjør at den ikke høres naken ut.

Kortere DECAY = hardere og kortere pluck."""),
("House-stab", """Akkord-stab som i klassisk house.

1. OSC 1 sag, OSC 2 sag en oktav opp, UNISON 3 stemmer på begge.
2. FILTER 1 (Analog 24dB), CUTOFF midt på, litt RESONANCE.
3. ENV 2 til CUTOFF med kort DECAY, som på pluck, men litt lengre.
4. ENV 1: ATTACK 0, DECAY ca. 0,4 s, SUSTAIN 0, RELEASE kort.
5. Spill akkorder med 3-4 toner.
6. EFFECTS: Reverb med kort DECAY TIME, litt Chorus."""),
("BASS", None),
("Sub-bass", """Den rene, dype bassen under alt annet.

1. Bruk bare OSC 1. UNISON 1 stemme.
2. Skru spektral-morfen (knotten nederst til venstre i oscillatoren) til Low Pass og vri helt ned. Da blir sagen til en ren sinus.
3. PITCH -12 eller -24 om du spiller høyt på tastaturet.
4. VOICES nederst til 1, og slå på LEGATO så tonene glir pent over i hverandre.
5. ENV 1: ATTACK bitte litt opp for å unngå klikk, RELEASE kort.
6. Ingen reverb eller chorus på sub. Hold den ren og i midten."""),
("Bass house-bass (FM)", """Den knurrende, metalliske bassen.

1. OSC 1: sag eller sinus (se Sub-bass), UNISON 1.
2. Skru på OSC 2, men sett LEVEL helt ned. Den skal ikke høres, bare forme OSC 1.
3. På OSC 1, bølge-morfen (knotten nederst til høyre): velg FM <- OSC 2 og skru opp.
4. Prøv PITCH på OSC 2: +12, +19 eller +24 gir helt forskjellig karakter.
5. Dra ENV 2 til FM-knotten med kort DECAY. Da biter lyden i starten av hver tone.
6. EFFECTS: Distortion på, DRIVE opp. Compressor på.
7. VOICES 1.

Mer FM = mer metall. Mer DRIVE = mer skitt."""),
("Donk-bass", """Den hule, sprettende bassen fra bassline og speed garage.

1. Lag en sinus på OSC 1 (se Sub-bass).
2. OSC 2 med LEVEL helt ned, PITCH +12.
3. OSC 1: velg FM <- OSC 2 på bølge-morfen, mengde lavt.
4. Dra ENV 2 til FM-mengden. ENV 2: ATTACK 0, DECAY veldig kort (0,05-0,15 s), SUSTAIN 0.
5. ENV 1: DECAY kort, SUSTAIN lavt.
6. Litt Distortion for å få den frem.

Selve donk-lyden er FM-envelopen. Juster DECAY på ENV 2 til den sier donk."""),
("Reese-bass", """Den mørke, bølgende bassen.

1. OSC 1 og OSC 2: begge sag, samme PITCH.
2. UNISON 2 stemmer på hver, detune 10-20 %. Det er de små forskjellene som lager bølgingen.
3. FILTER 1 (Analog 24dB), CUTOFF lavt.
4. Dra LFO 1 til CUTOFF, sakte hastighet (1/1 eller 2/1), liten mengde.
5. EFFECTS: Distortion lett, Chorus av, Compressor på.
6. Legg gjerne en egen sub-bass under, og kutt bunnen på reesen med EQ."""),
("808", """Lang bass med et lite spark i starten.

1. Sinus på OSC 1 (se Sub-bass), VOICES 1.
2. Dra ENV 2 til PITCH på OSC 1, mengde ca. +12 til +24.
3. ENV 2: ATTACK 0, DECAY veldig kort (0,03-0,08 s), SUSTAIN 0. Det gir sparket.
4. ENV 1: ATTACK 0, DECAY lang (1-2 s), SUSTAIN 0, RELEASE ca. 0,3 s.
5. Distortion med litt DRIVE gjør at den høres på små høyttalere."""),
("ANNET", None),
("Pad", """Myk bakgrunnslyd som fyller ut.

1. OSC 1 og 2: sag, UNISON 5 stemmer, detune 15-25 %.
2. ENV 1: ATTACK 0,5-1 s, SUSTAIN høyt, RELEASE 1-2 s.
3. FILTER 1 med CUTOFF midt på så den ikke blir for skarp.
4. Dra LFO 1 sakte til CUTOFF for litt liv.
5. EFFECTS: Chorus på, Reverb med høy MIX og lang DECAY TIME."""),
("Riser", """Lyden som bygger opp før droppet.

1. Skru av OSC 1 og slå på SMP (White Noise).
2. FILTER 1 på, send SMP til filteret, CUTOFF helt ned.
3. I FL: automatiser CUTOFF fra lavt til høyt over 4 eller 8 takter.
4. Legg til Reverb med mye MIX.
5. Vil du ha tone i riseren: slå på OSC 1 og automatiser PITCH oppover samtidig."""),
("Få det til å låte ferdig", """En rå synthlyd høres nesten alltid flat ut. Dette er det som gjør forskjellen:

1. Compressor (EFFECTS): det er en multiband-kompressor. Skru den på og prøv MIX rundt 30-50 %. Lyden blir lysere, tettere og mer i trynet.
2. Distortion: litt DRIVE gir varme og gjør at lyden høres på små høyttalere.
3. Bredde: UNISON og Chorus gjør lyden bred. Men hold bass og sub i midten.
4. Lag på lag: en god lead er ofte 2-3 lyder samtidig, f.eks. supersaw + pluck + en oktav over.
5. Plass i miksen: kutt bunnen (under ca. 150 Hz) på alt som ikke er bass eller kick.
6. Sidechain mot kicken i FL, så pumper det som en ordentlig house-låt."""),
]
def cstr(s):
    out = []
    for b in s.encode("utf-8"):
        c = chr(b)
        if c == "\n": out.append("\\n")
        elif c == '"': out.append('\\"')
        elif c == "\\": out.append("\\\\")
        elif 32 <= b < 127 and c != "?": out.append(c)
        else: out.append("\\%03o" % b)
    return '"' + "".join(out) + '"'
lines = ["// Generert av tools/help_content.py - ikke rediger for hand.", "#pragma once", "",
         "namespace tobbe_help {", "  struct Topic { const char* title; const char* body; };", "  static const Topic kTopics[] = {"]
for t, b in T:
    lines.append("    { %s, %s }," % (cstr(t), "nullptr" if b is None else cstr(b)))
lines += ["  };", "  static const int kNumTopics = %d;" % len(T), "}", ""]
(root / "src/interface/editor_sections/help_content.h").write_text("\n".join(lines))
print(len(T), "topics")
