# Datasets

Raw source corpora for bulk-importing scores via `manage.py add_scores` (see the main [README](../README.md#adding-scores)). Each subfolder is a self-contained corpus; see its section below for provenance, the exact import command, and which songs did/didn't import successfully.

## RS200 Harmony Corpus

The [Rock Corpus](https://rockcorpus.midside.com/harmonic_analyses.html) harmonic analyses (Trevor de Clercq & David Temperley), in Clercq-Temperley `.har` Roman-numeral notation. 200 songs from Rolling Stone's "500 Greatest Songs of All Time," each independently annotated twice — by David Temperley (`_dt`) and Trevor de Clercq (`_tdc`) — for 400 files total.

Imported into the app via:

```sh
python manage.py add_scores ../datasets/rs200_harmony har rs
```

### Import status

**393 of 400 files imported successfully.** The 7 that failed all involve harmony outside this corpus's normal scope: the RS200 annotations are built around **diatonic harmony** (chords expressible as plain triads or standard seventh chords within a key), and music21's Roman-numeral chord builder only constructs dominant-seventh chords from a fixed set of figures (`7`, `65`, `43`, `42`, `2`). The failing files use extended/altered dominant chords (9ths, an altered 9th, a 6th) that fall outside that diatonic vocabulary, which is outside the scope of the harmonic grammar this project focuses on. One additional file hit an unrelated parser edge case in a section reference.

| # | Song | dt | tdc |
|---|---|---|---|
| 1 | 11 My Generation | ✅ | ✅ |
| 2 | 1999 | ✅ | ✅ |
| 3 | A Change is Gonna Come | ✅ | ✅ |
| 4 | A Day in the Life | ✅ | ✅ |
| 5 | A Hard Day's Night | ✅ | ✅ |
| 6 | All Along the Watchtower | ✅ | ✅ |
| 7 | All Apologies | ✅ | ✅ |
| 8 | All I Have to do is Dream | ✅ | ✅ |
| 9 | Anarchy in the UK | ✅ | ✅ |
| 10 | Back in Black | ✅ | ✅ |
| 11 | Be Bop A Lula | ✅ | ✅ |
| 12 | Be My Baby | ✅ | ✅ |
| 13 | Beatles, Yesterday | ✅ | ✅ |
| 14 | Billie Jean | ✅ | ✅ |
| 15 | Bittersweet Symphony | ✅ | ✅ |
| 16 | Bizarre Love Triangle | ✅ | ✅ |
| 17 | Blitzkrieg Bop | ✅ | ✅ |
| 18 | Blue Suede Shoes | ✅ | ✅ |
| 19 | Blueberry Hill | ✅ | ✅ |
| 20 | Bo Diddley | ✅ | ✅ |
| 21 | Bohemian Rhapsody | ✅ | ✅ |
| 22 | Born to be Wild | ✅ | ✅ |
| 23 | Born to Run | ✅ | ✅ |
| 24 | Both Sides Now | ✅ | ✅ |
| 25 | Bridge Over Troubled Water | ✅ | ✅ |
| 26 | Brown-Eyed Girl | ✅ | ✅ |
| 27 | California Dreamin' | ✅ | ✅ |
| 28 | California Girls | ✅ | ✅ |
| 29 | California Love | ✅ | ✅ |
| 30 | Cathy's Clown | ✅ | ✅ |
| 31 | Changes | ✅ | ✅ |
| 32 | Come As You Are | ✅ | ✅ |
| 33 | Crazy | ✅ | ✅ |
| 34 | Crying | ✅ | ✅ |
| 35 | Da Doo Ron Ron | ✅ | ✅ |
| 36 | Dancing in the Street | ✅ | ✅ |
| 37 | Dancing Queen | ✅ | ✅ |
| 38 | Dock of the Bay | ✅ | ✅ |
| 39 | Don't Worry Baby | ✅ | ✅ |
| 40 | Dream On | ✅ | ✅ |
| 41 | Dylan - Blowin' in the Wind | ✅ | ✅ |
| 42 | Earth Angel | ✅ | ✅ |
| 43 | Eight Miles High | ✅ | ✅ |
| 44 | Eleanor Rigby | ✅ | ✅ |
| 45 | Enter Sandman | ✅ | ✅ |
| 46 | Every Breath You Take | ✅ | ✅ |
| 47 | Everyday People | ✅ | ✅ |
| 48 | Fake Plastic Trees | ✅ | ✅ |
| 49 | Family Affair | ✅ | ✅ |
| 50 | Fast Car | ✅ | ✅ |
| 51 | Folsom Prison Blues | ✅ | ✅ |
| 52 | For What Its Worth | ✅ | ✅ |
| 53 | Fortunate Son | ✅ | ✅ |
| 54 | Foxey Lady | ✅ | ❌ extended chord (`d7#9`) outside music21's supported dominant-seventh figures |
| 55 | Free Fallin' | ✅ | ✅ |
| 56 | Georgia On My Mind | ✅ | ✅ |
| 57 | Gimme Shelter | ✅ | ✅ |
| 58 | Go Your Own Way | ✅ | ✅ |
| 59 | God Only Knows | ✅ | ✅ |
| 60 | God Save the Queen | ✅ | ✅ |
| 61 | Good Golly Miss Molly | ✅ | ✅ |
| 62 | Good Vibrations | ✅ | ✅ |
| 63 | Great Balls of Fire | ✅ | ✅ |
| 64 | Hallelujah | ✅ | ✅ |
| 65 | Heartbreak Hotel | ✅ | ✅ |
| 66 | Help | ✅ | ✅ |
| 67 | Heroes | ✅ | ✅ |
| 68 | Hey Jude | ✅ | ✅ |
| 69 | Honky Tonk Women | ✅ | ✅ |
| 70 | Hot Stuff | ✅ | ✅ |
| 71 | Hotel California | ✅ | ✅ |
| 72 | Hound Dog | ✅ | ✅ |
| 73 | House of the Rising Sun | ✅ | ✅ |
| 74 | I Believe I Can Fly | ✅ | ✅ |
| 75 | I Can't Make You Love Me | ✅ | ✅ |
| 76 | I Can't Stop Loving You | ✅ | ✅ |
| 77 | I Fought the Law | ✅ | ✅ |
| 78 | I Got You | ✅ | ✅ |
| 79 | I Heard it Through the Grapevine | ✅ | ✅ |
| 80 | I Only Have Eyes | ✅ | ✅ |
| 81 | I Saw Her Standing There | ✅ | ✅ |
| 82 | I Still Haven't Found What I'm Looking For | ✅ | ✅ |
| 83 | I Walk the Line | ✅ | ✅ |
| 84 | I Wanna Be Sedated | ✅ | ✅ |
| 85 | I Wanna Hold Your Hand | ✅ | ✅ |
| 86 | I Want You Back | ✅ | ✅ |
| 87 | I'm So Lonesome | ✅ | ✅ |
| 88 | I'm Waiting for the Man | ✅ | ✅ |
| 89 | I've Been Loving You | ✅ | ✅ |
| 90 | Imagine | ✅ | ✅ |
| 91 | In Bloom | ✅ | ✅ |
| 92 | In My Life | ✅ | ✅ |
| 93 | In The Midnight Hour | ✅ | ✅ |
| 94 | In the Still of the Night | ✅ | ✅ |
| 95 | It's A Man's World | ✅ | ✅ |
| 96 | Jailhouse Rock | ✅ | ✅ |
| 97 | Jimi Hendrix, Purple Haze | ✅ | ✅ |
| 98 | Johnny B. Goode | ✅ | ✅ |
| 99 | Jumpin' Jack Flash | ✅ | ✅ |
| 100 | Kashmir | ✅ | ✅ |
| 101 | Layla | ✅ | ✅ |
| 102 | Let it Be | ✅ | ✅ |
| 103 | Let's Get it On | ✅ | ✅ |
| 104 | Let's Stay Together | ✅ | ❌ extended chord (`d9`) outside music21's supported dominant-seventh figures |
| 105 | Light my Fire | ✅ | ✅ |
| 106 | Like A Rolling Stone | ✅ | ✅ |
| 107 | Little Red Corvette | ✅ | ✅ |
| 108 | Living for the City | ✅ | ✅ |
| 109 | London Calling | ✅ | ✅ |
| 110 | Long Tall Sally | ✅ | ✅ |
| 111 | Lose Yourself | ✅ | ✅ |
| 112 | Loser | ✅ | ✅ |
| 113 | Losing My Religion | ✅ | ✅ |
| 114 | Louie Louie | ✅ | ✅ |
| 115 | Love and Happiness | ✅ | ✅ |
| 116 | Love Will Tear Us Apart | ✅ | ✅ |
| 117 | Lust for Life | ✅ | ✅ |
| 118 | Maggie May | ✅ | ✅ |
| 119 | Maybelline | ✅ | ✅ |
| 120 | Me and Bobby McGee | ✅ | ✅ |
| 121 | Mr Tambourine Man (Dylan) | ✅ | ✅ |
| 122 | Mr. Tambourine Man (Byrds) | ✅ | ✅ |
| 123 | My Girl | ✅ | ✅ |
| 124 | Mystery Train | ✅ | ✅ |
| 125 | No Woman No Cry | ✅ | ✅ |
| 126 | Norwegian Wood | ✅ | ✅ |
| 127 | Not Fade Away | ✅ | ✅ |
| 128 | Nothing Compares 2 U | ✅ | ✅ |
| 129 | Nuthin But a G Thang | ✅ | ✅ |
| 130 | One | ✅ | ✅ |
| 131 | Paint it Black | ✅ | ✅ |
| 132 | Papa Was a Rolling Stone | ✅ | ✅ |
| 133 | Papa's Got a Brand New Bag | ✅ | ✅ |
| 134 | Paranoid Android | ✅ | ✅ |
| 135 | People Get Ready | ✅ | ✅ |
| 136 | Please Please Please | ✅ | ✅ |
| 137 | Proud Mary | ✅ | ✅ |
| 138 | Purple Rain | ✅ | ✅ |
| 139 | Rave On | ✅ | ✅ |
| 140 | Redemption Song | ✅ | ✅ |
| 141 | Respect | ✅ | ✅ |
| 142 | Ring Of Fire | ✅ | ✅ |
| 143 | River Deep Mountain High | ✅ | ✅ |
| 144 | Rock and Roll Music | ✅ | ✅ |
| 145 | Rock Around the Clock | ✅ | ✅ |
| 146 | Rock Lobster | ✅ | ✅ |
| 147 | Rockin in the Free World | ✅ | ✅ |
| 148 | Roll Over Beethoven | ✅ | ✅ |
| 149 | Sabotage | ✅ | ✅ |
| 150 | Satisfaction | ✅ | ✅ |
| 151 | September Gurls | ✅ | ✅ |
| 152 | Shake Rattle and Roll | ✅ | ✅ |
| 153 | She Loves You | ✅ | ✅ |
| 154 | Should I Stay or Should I Go | ✅ | ✅ |
| 155 | Shout | ✅ | ✅ |
| 156 | Smells Like Teen Spirit | ✅ | ✅ |
| 157 | Sounds of Silence | ✅ | ✅ |
| 158 | Stairway to Heaven | ✅ | ✅ |
| 159 | Stand By Me | ✅ | ✅ |
| 160 | Strawberry Fields Forever | ✅ | ✅ |
| 161 | Summer Babe | ✅ | ✅ |
| 162 | Summertime Blues | ✅ | ✅ |
| 163 | Sunshine of your Love | ✅ | ✅ |
| 164 | Superstition | ✅ | ✅ |
| 165 | Suspicious Minds | ✅ | ✅ |
| 166 | Sweet Child O' Mine | ✅ | ✅ |
| 167 | Sympathy for the Devil | ✅ | ✅ |
| 168 | Take Me to the River | ✅ | ✅ |
| 169 | Tangled Up in Blue | ✅ | ❌ extended chord (`d9`) outside music21's supported dominant-seventh figures |
| 170 | Tears in Heaven | ✅ | ❌ extended chord (`d6`) outside music21's supported dominant-seventh figures |
| 171 | That'll Be The Day | ✅ | ✅ |
| 172 | That's All Right | ✅ | ✅ |
| 173 | The Boxer | ✅ | ❌ extended chord (`d9`) outside music21's supported dominant-seventh figures |
| 174 | The Message | ❌ parser error (`list index out of range`) in a section reference | ✅ |
| 175 | The Times They Are A Changin | ✅ | ✅ |
| 176 | The Tracks of my Tears | ✅ | ✅ |
| 177 | The Weight | ✅ | ✅ |
| 178 | Thunder Road | ✅ | ✅ |
| 179 | Tutti Frutti | ✅ | ✅ |
| 180 | Up on the Roof | ✅ | ✅ |
| 181 | Voodoo Child | ✅ | ✅ |
| 182 | Walk On By | ✅ | ✅ |
| 183 | Waterloo Sunset | ✅ | ✅ |
| 184 | What'd I Say | ✅ | ✅ |
| 185 | What's Going On | ✅ | ✅ |
| 186 | When a Man Loves a Woman | ✅ | ✅ |
| 187 | When Doves Cry | ✅ | ✅ |
| 188 | While My Guitar Gently Weeps | ✅ | ✅ |
| 189 | Whiter Shade of Pale | ✅ | ✅ |
| 190 | Who Do You Love | ✅ | ✅ |
| 191 | Whole Lotta Love | ✅ | ✅ |
| 192 | Whole Lotta Shakin Goin On | ✅ | ✅ |
| 193 | Will You Love Me Tomorrow | ✅ | ✅ |
| 194 | With or Without You | ✅ | ✅ |
| 195 | Won't Get Fooled Again | ✅ | ✅ |
| 196 | You Can't Always Get You What You Want | ✅ | ✅ |
| 197 | You Really Got Me | ✅ | ✅ |
| 198 | You Send Me | ✅ | ✅ |
| 199 | You've Lost that Lovin' Feeling | ✅ | ❌ extended chord (`d9`) outside music21's supported dominant-seventh figures |
| 200 | Your Song | ✅ | ✅ |

## McGill Billboard Corpus

The [McGill Billboard Project](https://ddmal.ca/research/The_McGill_Billboard_Project_(Chord_Analysis_Dataset)/) chord analysis dataset: 890 songs sampled from the Billboard "Hot 100" charts (1958-1991), each annotated with structural sections and chords in SALAMI format. Each song ships as its own numbered folder containing a `salami_chords.txt` file.

Imported into the app via:

```sh
python manage.py add_scores ../datasets/McGill-Billboard txt billboard
```

(`add_scores` walks subdirectories to support this per-song-folder layout — see `backend/app/management/commands/add_scores.py`.)

### Import status

**878 of 890 songs imported successfully.** The 12 scores were not imported due to conflict between the specific chord voicings in this corpus's annotations and music21 parser.

- **10 songs** — music21 couldn't invert a chord as annotated (`Could not invert chord...inversion may not exist`), typically a slash-chord bass note that doesn't correspond to any note already in the chord.
- **2 songs** — an internal music21 parsing error (`'NoneType' object is not subscriptable`) on a specific chord annotation.

| # | Song | Artist | id | Status |
|---|---|---|---|---|
| 1 | (I was) Born To Cry | Dion | 1101 | ✅ |
| 2 | (Last Night) I Didn't Get To Sleep At All | The 5th Dimension | 0265 | ✅ |
| 3 | (Marie's the Name) His Latest Flame | Elvis Presley | 0617 | ✅ |
| 4 | (Marie's the Name) His Latest Flame | Elvis Presley | 0730 | ✅ |
| 5 | (Night Time Is) The Right Time | Ray Charles | 0214 | ✅ |
| 6 | (Sittin' On) The Dock Of The Bay | Otis Redding | 0645 | ✅ |
| 7 | (You're My) Soul And Inspiration | The Righteous Brothers | 0785 | ✅ |
| 8 | (You're My) Soul And Inspiration | The Righteous Brothers | 1151 | ✅ |
| 9 | (You're So Square) Baby, I Don't Care | Joni Mitchell | 0417 | ✅ |
| 10 | (Your Love Has Lifted Me) Higher And Higher | Rita Coolidge | 0336 | ✅ |
| 11 | 20-75 | Willie Mitchell | 1247 | ✅ |
| 12 | 25 Or 6 To 4 | Chicago | 0176 | ✅ |
| 13 | 25 Or 6 To 4 | Chicago | 0292 | ✅ |
| 14 | 25 Or 6 To 4 | Chicago | 1227 | ✅ |
| 15 | 50 Ways To Leave Your Lover | Paul Simon | 0824 | ✅ |
| 16 | A Cowboys Work Is Never Done | Sonny & Cher | 1147 | ✅ |
| 17 | A Dream Goes On Forever | Todd Rundgren | 0895 | ❌ Could not invert chord...inversion may not exist |
| 18 | A Hard Day's Night | The Beatles | 1142 | ✅ |
| 19 | A Hazy Shade Of Winter | Simon & Garfunkel | 1121 | ✅ |
| 20 | A Lesson In Leavin' | Dottie West | 0101 | ✅ |
| 21 | A Trick Of The Night | Bananarama | 0099 | ✅ |
| 22 | A Very Special Love Song | Charlie Rich | 0779 | ✅ |
| 23 | Abacab | Genesis | 1256 | ✅ |
| 24 | Abraham, Martin And John | Dion | 1146 | ✅ |
| 25 | Absolutely Right | Five Man Electrical Band | 0041 | ✅ |
| 26 | Addicted To Love | Robert Palmer | 0271 | ✅ |
| 27 | Addicted To Love | Robert Palmer | 0458 | ✅ |
| 28 | After The Love Has Gone | Earth, Wind & Fire | 1056 | ✅ |
| 29 | After The Love Has Gone | Earth, Wind & Fire | 1097 | ✅ |
| 30 | After The Lovin' | Engelbert Humperdinck | 0506 | ✅ |
| 31 | After The Lovin' | Engelbert Humperdinck | 0636 | ✅ |
| 32 | Against The Wind | Bob Seger | 1177 | ✅ |
| 33 | Ain't No Sunshine | Bill Withers | 1058 | ✅ |
| 34 | Ain't Too Proud To Beg | The Temptations | 0468 | ✅ |
| 35 | Alive Again | Chicago | 1240 | ✅ |
| 36 | All Alone Am I | Brenda Lee | 1253 | ✅ |
| 37 | All I Ever Need Is You | Sonny & Cher | 0950 | ✅ |
| 38 | All She Wants Is | Duran Duran | 0592 | ✅ |
| 39 | All She Wants Is | Duran Duran | 1226 | ✅ |
| 40 | All This Time | Sting | 1012 | ✅ |
| 41 | All Those Years Ago | George Harrison | 0517 | ✅ |
| 42 | All Those Years Ago | George Harrison | 0680 | ✅ |
| 43 | All Through The Night | Cyndi Lauper | 0309 | ✅ |
| 44 | All Through The Night | Cyndi Lauper | 0769 | ✅ |
| 45 | All Through The Night | Cyndi Lauper | 1084 | ✅ |
| 46 | Almost Grown | Chuck Berry | 0792 | ✅ |
| 47 | Almost Like Being In Love | Michael Johnson | 0547 | ✅ |
| 48 | Along Comes A Woman | Chicago | 0198 | ✅ |
| 49 | Along Comes A Woman | Chicago | 0574 | ✅ |
| 50 | Along Comes A Woman | Chicago | 0776 | ✅ |
| 51 | Already Gone | Eagles | 0209 | ✅ |
| 52 | Always On My Mind | Pet Shop Boys | 0184 | ✅ |
| 53 | Always Something There To Remind Me | Naked Eyes | 0181 | ✅ |
| 54 | Amanda | Boston | 1234 | ✅ |
| 55 | American Storm | Bob Seger | 1277 | ✅ |
| 56 | Amie | Pure Prairie League | 0406 | ✅ |
| 57 | Amor | Ben E. King | 0583 | ✅ |
| 58 | An Innocent Man | Billy Joel | 0010 | ✅ |
| 59 | And She Was | Talking Heads | 0023 | ✅ |
| 60 | And She Was | Talking Heads | 0870 | ✅ |
| 61 | Annie's Song | John Denver | 0182 | ✅ |
| 62 | Another Brick In The Wall (Part II) | Pink Floyd | 1052 | ✅ |
| 63 | Another Rainy Day In New York City | Chicago | 0208 | ✅ |
| 64 | Are You Sure Hank Done It This Way | Waylon Jennings | 1139 | ✅ |
| 65 | As Usual | Brenda Lee | 0288 | ✅ |
| 66 | As Usual | Brenda Lee | 0471 | ✅ |
| 67 | Ask Me | Elvis Presley | 0658 | ✅ |
| 68 | Ask Me | Elvis Presley | 0766 | ✅ |
| 69 | Baby Can I Hold You | Tracy Chapman | 0747 | ✅ |
| 70 | Baby Come Back | Player | 1003 | ✅ |
| 71 | Baby Don't Change Your Mind | Gladys Knight & The Pips | 0705 | ✅ |
| 72 | Baby Don't Change Your Mind | Gladys Knight & The Pips | 0888 | ✅ |
| 73 | Baby Don't Change Your Mind | Gladys Knight & The Pips | 1250 | ✅ |
| 74 | Baby Don't Forget My Number | Milli Vanilli | 1276 | ✅ |
| 75 | Baby Don't Go | Sonny & Cher | 1212 | ✅ |
| 76 | Baby I'm Burnin' | Dolly Parton | 0559 | ✅ |
| 77 | Baby I'm Burnin' | Dolly Parton | 0987 | ✅ |
| 78 | Baby What You Want Me To Do | Jimmy Reed | 1024 | ✅ |
| 79 | Baby What You Want Me To Do | Jimmy Reed | 1263 | ✅ |
| 80 | Baby Workout | Jackie Wilson | 0672 | ✅ |
| 81 | Baby, Baby Don't Cry | The Miracles | 0481 | ✅ |
| 82 | Baby, Baby Don't Cry | The Miracles | 1186 | ✅ |
| 83 | Baby, You're Right | James Brown | 0533 | ✅ |
| 84 | Back Home Again | John Denver | 0235 | ✅ |
| 85 | Back Home Again | John Denver | 0446 | ✅ |
| 86 | Back In The High Life Again | Steve Winwood | 0207 | ✅ |
| 87 | Bad Moon Rising | Creedence Clearwater Revival | 0852 | ✅ |
| 88 | Be My Baby | The Ronettes | 0120 | ✅ |
| 89 | Be My Baby | The Ronettes | 0903 | ✅ |
| 90 | Be My Guest | Fats Domino | 1072 | ✅ |
| 91 | Beat It | Michael Jackson | 0629 | ✅ |
| 92 | Beautiful | Gordon Lightfoot | 0180 | ✅ |
| 93 | Because I Love You (The Postman Song) | Stevie B | 0242 | ✅ |
| 94 | Because I Love You (The Postman Song) | Stevie B | 0782 | ✅ |
| 95 | Behind Closed Doors | Charlie Rich | 1218 | ✅ |
| 96 | Best Of My Love | Eagles | 1061 | ✅ |
| 97 | Best Thing That Ever Happened To Me | Gladys Knight & The Pips | 0380 | ❌ Could not invert chord...inversion may not exist |
| 98 | Better Things | The Kinks | 0443 | ✅ |
| 99 | Big Iron | Marty Robbins | 0814 | ✅ |
| 100 | Big Iron | Marty Robbins | 1120 | ✅ |
| 101 | Big Yellow Taxi | Joni Mitchell | 0668 | ✅ |
| 102 | Bird Dog | The Everly Brothers | 0322 | ✅ |
| 103 | Bird Dog | The Everly Brothers | 0733 | ✅ |
| 104 | Black Cars | Gino Vannelli | 0068 | ✅ |
| 105 | Blow Away | George Harrison | 0419 | ✅ |
| 106 | Blue Eyes Crying In The Rain | Willie Nelson | 0126 | ✅ |
| 107 | Blue Jean | David Bowie | 0818 | ✅ |
| 108 | Bluebirds Over The Mountain | The Beach Boys | 0427 | ✅ |
| 109 | Bongo Stomp | Little Joey & The Flips | 0067 | ✅ |
| 110 | Born To Be Alive | Patrick Hernandez | 0259 | ✅ |
| 111 | Born To Be Alive | Patrick Hernandez | 0279 | ✅ |
| 112 | Born To Be Alive | Patrick Hernandez | 0552 | ✅ |
| 113 | Born To Be Wild | Steppenwolf | 0841 | ✅ |
| 114 | Boulevard | Jackson Browne | 0561 | ✅ |
| 115 | Boulevard | Jackson Browne | 0695 | ✅ |
| 116 | Brandy (You're A Fine Girl) | Looking Glass | 0128 | ✅ |
| 117 | Brandy (You're A Fine Girl) | Looking Glass | 0682 | ✅ |
| 118 | Brass Monkey | Beastie Boys | 0634 | ✅ |
| 119 | Break It To Me Gently | Juice Newton | 0303 | ✅ |
| 120 | Breaking Up Is Hard To Do | Neil Sedaka | 0728 | ✅ |
| 121 | Breezin' | George Benson | 0967 | ✅ |
| 122 | Burning Down The House | Talking Heads | 0844 | ✅ |
| 123 | Bust A Move | Young MC | 1106 | ✅ |
| 124 | Buy For Me The Rain | Nitty Gritty Dirt Band | 0088 | ✅ |
| 125 | California Nights | Lesley Gore | 0813 | ✅ |
| 126 | California Nights | Lesley Gore | 0896 | ✅ |
| 127 | Can We Still Be Friends | Todd Rundgren | 1076 | ✅ |
| 128 | Carrie | Cliff Richard | 0051 | ✅ |
| 129 | Carrie | Cliff Richard | 1222 | ✅ |
| 130 | Carrie-Anne | The Hollies | 0477 | ✅ |
| 131 | Carry Me | David Crosby,Graham Nash | 1124 | ✅ |
| 132 | Catch My Fall | Billy Idol | 0794 | ✅ |
| 133 | Caught Up In The Rapture | Anita Baker | 0647 | ✅ |
| 134 | Caught Up In The Rapture | Anita Baker | 0709 | ✅ |
| 135 | Cecilia | Simon & Garfunkel | 0560 | ✅ |
| 136 | Chain Of Fools | Aretha Franklin | 0418 | ✅ |
| 137 | Chained And Bound | Otis Redding | 0678 | ✅ |
| 138 | Chicago | Graham Nash | 0025 | ✅ |
| 139 | Chiquitita | Abba | 0183 | ✅ |
| 140 | City In The Sky | The Staple Singers | 0497 | ✅ |
| 141 | Cold Sweat - Part 1 | James Brown | 0079 | ✅ |
| 142 | Come And Get Your Love | Redbone | 0315 | ✅ |
| 143 | Come Monday | Jimmy Buffett | 0758 | ✅ |
| 144 | Come Together | The Beatles | 0473 | ✅ |
| 145 | Comin' Home Baby | Mel Torme | 0213 | ✅ |
| 146 | Coming On Strong | Brenda Lee | 0968 | ✅ |
| 147 | Could I Have This Dance | Anne Murray | 0199 | ✅ |
| 148 | Count On Me | Jefferson Starship | 1045 | ✅ |
| 149 | Country Road | James Taylor | 0901 | ✅ |
| 150 | Crackerbox Palace | George Harrison | 1282 | ✅ |
| 151 | Crazy On You | Heart | 0033 | ✅ |
| 152 | Crazy On You | Heart | 0073 | ✅ |
| 153 | Cruisin' | Smokey Robinson | 0307 | ✅ |
| 154 | Cruisin' | Smokey Robinson | 1133 | ✅ |
| 155 | Cruisin' | Smokey Robinson | 1162 | ✅ |
| 156 | Cry Like A Baby | The Box Tops | 0935 | ✅ |
| 157 | Cry Softly Lonely One | Roy Orbison | 0064 | ✅ |
| 158 | Crying Time | Ray Charles | 0748 | ✅ |
| 159 | Crystal Blue Persuasion | Tommy James | 0528 | ✅ |
| 160 | D'yer Mak'er | Led Zeppelin | 0749 | ✅ |
| 161 | Daddy's Home | Cliff Richard | 1161 | ✅ |
| 162 | Dance Away | Roxy Music | 0568 | ✅ |
| 163 | Dance Away | Roxy Music | 0846 | ✅ |
| 164 | Dance Hall Days | Wang Chung | 0886 | ✅ |
| 165 | Dancing Machine | The Jacksons | 0985 | ✅ |
| 166 | Dandelion | The Rolling Stones | 0264 | ✅ |
| 167 | Daydream Believer | Anne Murray | 0312 | ✅ |
| 168 | Daydream Believer | Anne Murray | 0475 | ✅ |
| 169 | Deeper Shade Of Soul | Urban Dance Squad | 0339 | ✅ |
| 170 | Detroit City | Bobby Bare | 0133 | ✅ |
| 171 | Devil Woman | Cliff Richard | 1073 | ✅ |
| 172 | Dial My Heart | The Boys | 0078 | ✅ |
| 173 | Dirty Water | Rock And Hyde | 0929 | ✅ |
| 174 | Disco Inferno | The Trammps | 0546 | ✅ |
| 175 | Disco Inferno | The Trammps | 1016 | ✅ |
| 176 | Do I Do | Stevie Wonder | 0736 | ✅ |
| 177 | Do You Love Me | The Contours | 0066 | ✅ |
| 178 | Do You Love Me | The Contours | 0335 | ✅ |
| 179 | Do You Love Me | The Contours | 0849 | ✅ |
| 180 | Do You Want To Know A Secret | The Beatles | 0302 | ✅ |
| 181 | Do Your Thing | Isaac Hayes | 0216 | ✅ |
| 182 | Does Anybody Really Know What Time It Is? | Chicago | 0700 | ✅ |
| 183 | Don t Treat Me Bad | Firehouse | 0349 | ✅ |
| 184 | Don't Ask Me Why | Billy Joel | 0969 | ✅ |
| 185 | Don't Knock My Love - Pt. 1 | Wilson Pickett | 0677 | ✅ |
| 186 | Don't Leave Me This Way | Thelma Houston | 1086 | ✅ |
| 187 | Don't Say You Love Me | Billy Squier | 0452 | ✅ |
| 188 | Don't Stand So Close To Me | The Police | 0492 | ✅ |
| 189 | Don't Stand So Close To Me | The Police | 0881 | ✅ |
| 190 | Don't Talk To Strangers | Rick Springfield | 0865 | ✅ |
| 191 | Don't Treat Me Bad | Firehouse | 0258 | ✅ |
| 192 | Don't You Know What The Night Can Do? | Steve Winwood | 0889 | ✅ |
| 193 | Doo Doo Doo Doo Doo (Heartbreaker) | The Rolling Stones | 0345 | ✅ |
| 194 | Double Shot (Of My Baby's Love) | Swingin' Medallions | 0549 | ✅ |
| 195 | Down And Out In New York City | James Brown | 1032 | ✅ |
| 196 | Dream Police | Cheap Trick | 0317 | ✅ |
| 197 | Dream Police | Cheap Trick | 0323 | ✅ |
| 198 | Drivin' Wheel | Foghat | 0075 | ✅ |
| 199 | Drivin' Wheel | Foghat | 0095 | ✅ |
| 200 | Dum Dum | Brenda Lee | 0356 | ✅ |
| 201 | Easy | Commodores | 0341 | ✅ |
| 202 | Easy | Commodores | 1157 | ✅ |
| 203 | Ebony Eyes | The Everly Brothers | 1116 | ✅ |
| 204 | Ebony Eyes | The Everly Brothers | 1297 | ✅ |
| 205 | Echoes Of Love | The Doobie Brothers | 1200 | ✅ |
| 206 | Eight Days A Week | The Beatles | 0727 | ✅ |
| 207 | Eight Miles High | The Byrds | 0111 | ✅ |
| 208 | El Condor Pasa | Simon & Garfunkel | 1261 | ✅ |
| 209 | Eleanor Rigby | Ray Charles | 0933 | ✅ |
| 210 | Elvira | Oak Ridge Boys | 0864 | ✅ |
| 211 | Even Now | Bob Seger | 1208 | ✅ |
| 212 | Everlasting Love | Carl Carlton | 0607 | ✅ |
| 213 | Every Little Thing She Does Is Magic | The Police | 0293 | ✅ |
| 214 | Every Time I Think Of You | The Babys | 1070 | ✅ |
| 215 | Everybody Loves Me But You | Brenda Lee | 0790 | ✅ |
| 216 | Everybody Loves Somebody | Dean Martin | 0618 | ✅ |
| 217 | Evil Ways | Santana | 0364 | ✅ |
| 218 | Eye In The Sky | The Alan Parsons Project | 0956 | ✅ |
| 219 | Fakin' It | Simon & Garfunkel | 0947 | ✅ |
| 220 | Feel Like Makin' Love | Roberta Flack | 0221 | ✅ |
| 221 | Feel Like Makin' Love | Roberta Flack | 0454 | ✅ |
| 222 | Feel Like Makin' Love | Roberta Flack | 0940 | ✅ |
| 223 | Feelin' Satisfied | Boston | 0952 | ✅ |
| 224 | Feelin' Stronger Every Day | Chicago | 0366 | ✅ |
| 225 | Feelin' Stronger Every Day | Chicago | 0684 | ✅ |
| 226 | Fernando | Abba | 0218 | ✅ |
| 227 | Fever | Peggy Lee | 0396 | ✅ |
| 228 | Fever | Rita Coolidge | 0692 | ✅ |
| 229 | Fire And Ice | Pat Benatar | 0089 | ✅ |
| 230 | Flesh For Fantasy | Billy Idol | 0464 | ✅ |
| 231 | Floy Joy | The Supremes | 0320 | ✅ |
| 232 | Foggy Mountain Breakdown | Flatt & Scruggs | 0037 | ✅ |
| 233 | Foggy Mountain Breakdown | Flatt & Scruggs | 0759 | ✅ |
| 234 | Fool That I Am | Etta James | 0515 | ✅ |
| 235 | Fool That I Am | Etta James | 0562 | ✅ |
| 236 | For Ol' Times Sake | Elvis Presley | 0222 | ✅ |
| 237 | For Ol' Times Sake | Elvis Presley | 0508 | ✅ |
| 238 | For Ol' Times Sake | Elvis Presley | 1235 | ✅ |
| 239 | For The Good Times | Ray Price | 0102 | ✅ |
| 240 | For The Good Times | Ray Price | 0725 | ✅ |
| 241 | Forever Man | Eric Clapton | 0155 | ✅ |
| 242 | Frankenstein | Edgar Winter | 1268 | ✅ |
| 243 | Freedom | Jimi Hendrix | 0035 | ✅ |
| 244 | Freeze-Frame | The J. Geils Band | 1002 | ❌ 'NoneType' object is not subscriptable |
| 245 | Funny Girl | Barbra Streisand | 1118 | ✅ |
| 246 | Galveston | Glen Campbell | 0224 | ✅ |
| 247 | Get Ready | Rare Earth | 1220 | ✅ |
| 248 | Get Together | The Youngbloods | 0072 | ✅ |
| 249 | Get Together | The Youngbloods | 1136 | ✅ |
| 250 | Get Up (I Feel Like Being Like A) Sex Machine (Part 1) | James Brown | 0857 | ✅ |
| 251 | Getaway | Earth, Wind & Fire | 0735 | ✅ |
| 252 | Ghostbusters | Ray Parker Jr. | 0621 | ✅ |
| 253 | Girl I m Gonna Miss You | Milli Vanilli | 1039 | ✅ |
| 254 | Girl You Know It's True | Milli Vanilli | 0913 | ✅ |
| 255 | Give It To Me Baby | Rick James | 0480 | ✅ |
| 256 | Give To Live | Sammy Hagar | 0465 | ✅ |
| 257 | Giving You The Best That I Got | Anita Baker | 0578 | ✅ |
| 258 | Gloria | Laura Branigan | 0995 | ✅ |
| 259 | Go Where You Wanna Go | The 5th Dimension | 0330 | ✅ |
| 260 | Goin' Back | The Byrds | 1033 | ❌ Could not invert chord...inversion may not exist |
| 261 | Going To A Go-Go | The Rolling Stones | 0512 | ✅ |
| 262 | Going To Chicago Blues | Count Basie | 1149 | ✅ |
| 263 | Golden Years | David Bowie | 0415 | ✅ |
| 264 | Good Morning Starshine | Oliver | 0834 | ✅ |
| 265 | Good Vibrations | Marky Mark | 0352 | ✅ |
| 266 | Good Vibrations | Marky Mark | 0503 | ✅ |
| 267 | Goodbye Yellow Brick Road | Elton John | 0842 | ✅ |
| 268 | Got It Made | Crosby, Stills, Nash | 0451 | ✅ |
| 269 | Got My Mind Set On You | George Harrison | 0845 | ❌ 'NoneType' object is not subscriptable |
| 270 | Gotta Serve Somebody | Bob Dylan | 0282 | ✅ |
| 271 | Guitar Man | Elvis Presley | 0289 | ✅ |
| 272 | Hair | The Cowsills | 0770 | ✅ |
| 273 | Handy Man | Jimmy Jones | 0250 | ✅ |
| 274 | Happy Anniversary | Little River Band | 1174 | ✅ |
| 275 | Happy Jack | The Who | 0891 | ✅ |
| 276 | Happy Man | Greg Kihn Band | 1246 | ✅ |
| 277 | Happy Together | The Turtles | 1290 | ✅ |
| 278 | Harden My Heart | Quarterflash | 0608 | ✅ |
| 279 | Harden My Heart | Quarterflash | 0659 | ✅ |
| 280 | Have You Ever Loved Somebody | Freddie Jackson | 0122 | ✅ |
| 281 | Have You Seen Your Mother, Baby, Standing In The Shadow? | The Rolling Stones | 0244 | ✅ |
| 282 | He's A Rebel | The Crystals | 0404 | ✅ |
| 283 | He's A Rebel | The Crystals | 1091 | ✅ |
| 284 | He's So Fine | The Chiffons | 1292 | ✅ |
| 285 | He's So Shy | Pointer Sisters | 0663 | ✅ |
| 286 | Heart Full Of Soul | The Yardbirds | 0579 | ✅ |
| 287 | Heart In Hand | Brenda Lee | 0484 | ✅ |
| 288 | Heartaches | Bachman-Turner Overdrive | 0699 | ✅ |
| 289 | Heartbreaker | Pat Benatar | 1053 | ✅ |
| 290 | Heartbreaker | Pat Benatar | 1204 | ✅ |
| 291 | Heaven Must Have Sent You | Bonnie Pointer | 1232 | ✅ |
| 292 | Heaven's Just A Sin Away | The Kendalls | 0671 | ✅ |
| 293 | Hello Hello | The Sopwith "Camel" | 0964 | ✅ |
| 294 | Hello Stranger | Barbara Lewis | 0984 | ✅ |
| 295 | Hello, Dolly! | Louis Armstrong | 0650 | ✅ |
| 296 | Help Is On Its Way | Little River Band | 0187 | ✅ |
| 297 | Help Is On Its Way | Little River Band | 0721 | ✅ |
| 298 | Help! | The Beatles | 1244 | ✅ |
| 299 | Here Come Those Tears Again | Jackson Browne | 0395 | ✅ |
| 300 | Here I Go Again | Whitesnake | 0300 | ✅ |
| 301 | Here's Some Love | Tanya Tucker | 0019 | ✅ |
| 302 | Hey Stoopid | Alice Cooper | 0599 | ✅ |
| 303 | Hey You! Get Off My Mountain | The Dramatics | 1020 | ✅ |
| 304 | Hey! Baby | Bruce Channel | 0789 | ✅ |
| 305 | Higher Ground | Stevie Wonder | 0625 | ✅ |
| 306 | Hocus Pocus | Focus | 0381 | ✅ |
| 307 | Hocus Pocus | Focus | 0999 | ✅ |
| 308 | Hold On | Wilson Phillips | 0385 | ✅ |
| 309 | Hold On | Wilson Phillips | 0628 | ✅ |
| 310 | Hold On | Wilson Phillips | 0911 | ✅ |
| 311 | Honey, Honey | Abba | 0902 | ✅ |
| 312 | Honky Tonk Women | The Rolling Stones | 0229 | ✅ |
| 313 | Honky Tonk Women | The Rolling Stones | 1266 | ✅ |
| 314 | Hooked On A Feeling | B.J. Thomas | 1048 | ✅ |
| 315 | Hot Child In The City | Nick Gilder | 0615 | ✅ |
| 316 | Hot Child In The City | Nick Gilder | 0783 | ✅ |
| 317 | Hot Fun In The Summertime | Sly & The Family Stone | 0070 | ✅ |
| 318 | Hot In The City | Billy Idol | 0920 | ✅ |
| 319 | How Blue Can You Get | B.B. King | 0510 | ✅ |
| 320 | Human Nature | Michael Jackson | 0637 | ✅ |
| 321 | Hungry Eyes (From "Dirty Dancing") | Eric Carmen | 0791 | ✅ |
| 322 | Hurts To Be In Love | Gino Vannelli | 0062 | ✅ |
| 323 | Hurts To Be In Love | Gino Vannelli | 1067 | ✅ |
| 324 | I Adore Mi Amor | Color Me Badd | 0476 | ✅ |
| 325 | I Can Help | Billy Swan | 0601 | ✅ |
| 326 | I Can Help | Billy Swan | 1093 | ✅ |
| 327 | I Can't Drive 55 | Sammy Hagar | 0353 | ✅ |
| 328 | I Can't Stand It | Eric Clapton | 0898 | ✅ |
| 329 | I Can't Stand The Rain | Ann Peebles | 0377 | ✅ |
| 330 | I Cried A Tear | LaVern Baker | 0822 | ✅ |
| 331 | I Cried A Tear | LaVern Baker | 0954 | ✅ |
| 332 | I Cried A Tear | LaVern Baker | 1166 | ✅ |
| 333 | I Don't Blame You At All | The Miracles | 0582 | ✅ |
| 334 | I Don't Love You Anymore | Teddy Pendergrass | 0797 | ✅ |
| 335 | I Don't Mind | James Brown | 0003 | ✅ |
| 336 | I Don't Need You | Kenny Rogers | 0494 | ✅ |
| 337 | I Don't Want To Spoil The Party | The Beatles | 1213 | ✅ |
| 338 | I Don't Want Your Love | Duran Duran | 1148 | ✅ |
| 339 | I Drove All Night | Cyndi Lauper | 1011 | ✅ |
| 340 | I Found A Love | The Falcons | 0580 | ✅ |
| 341 | I Found A True Love | Wilson Pickett | 0943 | ✅ |
| 342 | I Got Stripes | Johnny Cash | 1160 | ✅ |
| 343 | I Got You (I Feel Good) | James Brown | 0314 | ✅ |
| 344 | I Had Too Much To Dream (Last Night) | The Electric Prunes | 0134 | ✅ |
| 345 | I Just Can't Stop Loving You | Michael Jackson With Siedah Garrett | 0085 | ✅ |
| 346 | I Like The Way (The Kissing Game) | Hi-Five | 0856 | ✅ |
| 347 | I Love | Tom T. Hall | 0606 | ✅ |
| 348 | I Love A Rainy Night | Eddie Rabbitt | 1143 | ✅ |
| 349 | I Love You So | Bobbi Martin | 0056 | ✅ |
| 350 | I m Goin  Down | Bruce Springsteen | 0426 | ✅ |
| 351 | I Never Loved A Man (The Way I Love You) | Aretha Franklin | 0403 | ✅ |
| 352 | I Put A Spell On You | Creedence Clearwater Revival | 0061 | ✅ |
| 353 | I Really Don't Want To Know | Elvis Presley | 0386 | ✅ |
| 354 | I Really Don't Want To Know | Elvis Presley | 0444 | ✅ |
| 355 | I Rise, I Fall | Johnny Tillotson | 0355 | ✅ |
| 356 | I Saw Her Standing There | The Beatles | 0853 | ✅ |
| 357 | I Second That Emotion | The Miracles | 0946 | ✅ |
| 358 | I Walk Alone | Marty Robbins | 1054 | ✅ |
| 359 | I Want A New Drug | Huey Lewis | 0430 | ✅ |
| 360 | I Want To Take You Higher | Ike & Tina Turner | 0204 | ✅ |
| 361 | I Want To Take You Higher | Ike & Tina Turner | 0360 | ✅ |
| 362 | I Want To Take You Higher | Sly & The Family Stone | 0614 | ✅ |
| 363 | I Want To Take You Higher | Ike & Tina Turner | 0996 | ✅ |
| 364 | I Want To Walk You Home | Fats Domino | 0773 | ✅ |
| 365 | I Want You | Marvin Gaye | 0319 | ✅ |
| 366 | I Want You | Marvin Gaye | 0795 | ✅ |
| 367 | I Want You Back | The Jacksons | 1178 | ✅ |
| 368 | I Want You To Want Me | Cheap Trick | 0188 | ✅ |
| 369 | I Will | Dean Martin | 0734 | ✅ |
| 370 | I Wish It Would Rain | The Temptations | 0900 | ✅ |
| 371 | I Won't Stand In Your Way | Stray Cats | 1197 | ✅ |
| 372 | I Wouldn't Have Missed It For The World | Ronnie Milsap | 0131 | ✅ |
| 373 | I'd Love To Change The World | Ten Years After | 0248 | ✅ |
| 374 | I'd Love To Change The World | Ten Years After | 0751 | ✅ |
| 375 | I'll Take You There | The Staple Singers | 0046 | ✅ |
| 376 | I'll Tumble 4 Ya | Culture Club | 1223 | ✅ |
| 377 | I'm In Love | Evelyn "Champagne" King | 0482 | ✅ |
| 378 | I'm In Love | Wilson Pickett | 1221 | ✅ |
| 379 | I've Been Everywhere | Hank Snow | 1059 | ✅ |
| 380 | I've Been Loving You Too Long (To Stop Now) | Otis Redding | 0502 | ✅ |
| 381 | I've Got A Tiger By The Tail | Buck Owens | 1225 | ✅ |
| 382 | I've Got Love On My Mind | Natalie Cole | 0177 | ✅ |
| 383 | I've Passed This Way Before | Jimmy Ruffin | 1044 | ✅ |
| 384 | If | Bread | 0106 | ✅ |
| 385 | If | Bread | 0988 | ✅ |
| 386 | If I Can Dream | Elvis Presley | 0543 | ✅ |
| 387 | If I Can't Have You | Yvonne Elliman | 0034 | ✅ |
| 388 | If I Could Build My Whole World Around You | Marvin Gaye,Tammi Terrell | 0619 | ✅ |
| 389 | If I Could Build My Whole World Around You | Marvin Gaye,Tammi Terrell | 1100 | ✅ |
| 390 | If I Could Build My Whole World Around You | Marvin Gaye,Tammi Terrell | 1117 | ✅ |
| 391 | If I Could Reach You | The 5th Dimension | 0433 | ❌ Could not invert chord...inversion may not exist |
| 392 | If I Could Turn Back Time | Cher | 0843 | ✅ |
| 393 | If I Were A Carpenter | Bobby Darin | 1265 | ✅ |
| 394 | If I Were Your Woman | Gladys Knight & The Pips | 0343 | ✅ |
| 395 | If Not You | Dr. Hook | 0914 | ✅ |
| 396 | If You Love Somebody Set Them Free | Sting | 0384 | ✅ |
| 397 | If You Need Me | Solomon Burke | 0160 | ✅ |
| 398 | If You Need Me | Solomon Burke | 0172 | ✅ |
| 399 | If You Really Love Me | Stevie Wonder | 0631 | ✅ |
| 400 | In My Room | The Beach Boys | 0270 | ✅ |
| 401 | In The Midnight Hour | Wilson Pickett | 1018 | ✅ |
| 402 | In The Navy | Village People | 0306 | ✅ |
| 403 | In Your Soul | Corey Hart | 0469 | ✅ |
| 404 | In Your Soul | Corey Hart | 0657 | ✅ |
| 405 | In-A-Gadda-Da-Vida | Iron Butterfly | 0261 | ✅ |
| 406 | Indiana Wants Me | R. Dean Taylor | 0030 | ✅ |
| 407 | Indiana Wants Me | R. Dean Taylor | 0537 | ✅ |
| 408 | Invisible Touch | Genesis | 1126 | ✅ |
| 409 | Is That All There Is | Peggy Lee | 0059 | ✅ |
| 410 | Is There Something I Should Know | Duran Duran | 1043 | ✅ |
| 411 | Island Of Lost Souls | Blondie | 1203 | ✅ |
| 412 | It Amazes Me | John Denver | 0245 | ✅ |
| 413 | It Keeps Right On A-Hurtin' | Johnny Tillotson | 1041 | ✅ |
| 414 | It Takes Two | Marvin Gaye,Kim Weston | 0280 | ✅ |
| 415 | It Takes Two | Rob Base | 1109 | ✅ |
| 416 | It's Gonna Work Out Fine | Ike & Tina Turner | 0212 | ✅ |
| 417 | It's Only Make Believe | Glen Campbell | 0623 | ✅ |
| 418 | It's Only Rock 'N Roll (But I Like It) | The Rolling Stones | 0039 | ✅ |
| 419 | It's Raining Men | The Weather Girls | 0651 | ✅ |
| 420 | It's Your Thing | The Isley Brothers | 0391 | ✅ |
| 421 | Jamie | Eddie Holland | 1046 | ✅ |
| 422 | Jessie's Girl | Rick Springfield | 0217 | ✅ |
| 423 | Jessie's Girl | Rick Springfield | 0450 | ✅ |
| 424 | Jimmy's Girl | Johnny Tillotson | 0410 | ✅ |
| 425 | Johnny Reb | Johnny Horton | 1287 | ✅ |
| 426 | Journey To The Center Of The Mind | The Amboy Dukes | 0828 | ✅ |
| 427 | Judy | Elvis Presley | 0565 | ✅ |
| 428 | Judy | Elvis Presley | 0923 | ✅ |
| 429 | Jump (for My Love) | The Pointer Sisters | 0448 | ✅ |
| 430 | Jump (for My Love) | The Pointer Sisters | 0850 | ✅ |
| 431 | Jungle Boogie | Kool & The Gang | 0331 | ✅ |
| 432 | Just A Dream | Jimmy Clanton | 0185 | ✅ |
| 433 | Just A Dream | Jimmy Clanton | 0805 | ✅ |
| 434 | Just A Friend | Biz Markie | 0827 | ✅ |
| 435 | Just Can't Wait | The J. Geils Band | 0021 | ✅ |
| 436 | Just Like Heaven | The Cure | 0359 | ✅ |
| 437 | Just Like Jesse James | Cher | 0821 | ✅ |
| 438 | Just The Way You Are | Billy Joel | 0240 | ✅ |
| 439 | Just The Way You Are | Billy Joel | 0295 | ✅ |
| 440 | Just When I Needed You Most | Randy Vanwarmer | 0149 | ✅ |
| 441 | Karma Chameleon | Culture Club | 0979 | ✅ |
| 442 | Kicks | Paul Revere & The Raiders | 1181 | ✅ |
| 443 | Kind Of A Drag | The Buckinghams | 0369 | ✅ |
| 444 | Kiss On My List | Daryl Hall & John Oates | 0018 | ✅ |
| 445 | Kisses On The Wind | Neneh Cherry | 0370 | ✅ |
| 446 | Kisses On The Wind | Neneh Cherry | 0909 | ✅ |
| 447 | Knowing Me, Knowing You | Abba | 0231 | ✅ |
| 448 | Ko-Ko Joe | Jerry Reed | 0713 | ✅ |
| 449 | Kokomo (From The "Cocktail" Soundtrack) | The Beach Boys | 0974 | ✅ |
| 450 | Kozmic Blues | Janis Joplin | 0397 | ✅ |
| 451 | La Grange | ZZ Top | 0140 | ✅ |
| 452 | Lady | Kenny Rogers | 1258 | ✅ |
| 453 | Lady (You Bring Me Up) | Commodores | 0716 | ✅ |
| 454 | Lambada | Kaoma | 1270 | ✅ |
| 455 | Land Of 1000 Dances | Chris Kenner | 1111 | ✅ |
| 456 | Last Child | Aerosmith | 0015 | ✅ |
| 457 | Last Dance | Donna Summer | 0501 | ✅ |
| 458 | Last Dance | Donna Summer | 1217 | ✅ |
| 459 | Last Dance | Donna Summer | 1242 | ✅ |
| 460 | Last Date | Floyd Cramer | 0788 | ✅ |
| 461 | Last Kiss | J. Frank Wilson & The Cavaliers | 0054 | ✅ |
| 462 | Last Kiss | J. Frank Wilson & The Cavaliers | 0247 | ✅ |
| 463 | Last Kiss | Wednesday | 0263 | ✅ |
| 464 | Last Kiss | Wednesday | 0362 | ✅ |
| 465 | Last Kiss | J. Frank Wilson & The Cavaliers | 0402 | ✅ |
| 466 | Lay Down Sally | Eric Clapton | 1040 | ✅ |
| 467 | Let It Rain | Eric Clapton | 0116 | ✅ |
| 468 | Let Me Get To Know You | Paul Anka | 0325 | ✅ |
| 469 | Let The Music Play | Shannon | 1279 | ✅ |
| 470 | Let's Get Serious | Jermaine Jackson | 0811 | ✅ |
| 471 | Let's Go Get Stoned | Ray Charles | 0890 | ✅ |
| 472 | Let's Work Together | Canned Heat | 0577 | ✅ |
| 473 | Letter Full Of Tears | Gladys Knight & The Pips | 0112 | ✅ |
| 474 | Letter Full Of Tears | Gladys Knight & The Pips | 0596 | ✅ |
| 475 | Levon | Elton John | 0752 | ✅ |
| 476 | Liar, Liar | The Castaways | 0848 | ✅ |
| 477 | Life Is A Carnival | The Band | 0234 | ✅ |
| 478 | Like A Rock | Bob Seger | 0941 | ✅ |
| 479 | Little Bit O' Soul | The Music Explosion | 0467 | ✅ |
| 480 | Little Sister | Elvis Presley | 0159 | ✅ |
| 481 | Little Too Late | Pat Benatar | 0973 | ✅ |
| 482 | Live To Tell | Madonna | 1173 | ✅ |
| 483 | Living Doll | Cliff Richard | 0740 | ✅ |
| 484 | Living In The Past | Jethro Tull | 0706 | ✅ |
| 485 | Living It Down | Freddy Fender | 0346 | ✅ |
| 486 | Lonely Eyes | Robert John | 0154 | ✅ |
| 487 | Lonely Weekends | Charlie Rich | 1113 | ✅ |
| 488 | Lonely Weekends | Charlie Rich | 1123 | ✅ |
| 489 | Long Dark Road | The Hollies | 0290 | ✅ |
| 490 | Look-Ka Py Py | The Meters | 1096 | ✅ |
| 491 | Lookin' For Love | Johnny Lee | 0012 | ✅ |
| 492 | Looking For A Love | The J. Geils Band | 0662 | ✅ |
| 493 | Looking For A Love | The J. Geils Band | 0664 | ✅ |
| 494 | Losing You | Brenda Lee | 0371 | ✅ |
| 495 | Love Came To Me | Dion | 0253 | ✅ |
| 496 | Love Came To Me | Dion | 1152 | ✅ |
| 497 | Love Comes Quickly | Pet Shop Boys | 0526 | ✅ |
| 498 | Love Is A Battlefield | Pat Benatar | 0741 | ✅ |
| 499 | Love Me Do | The Beatles | 0050 | ✅ |
| 500 | Love Me Warm And Tender | Paul Anka | 0196 | ✅ |
| 501 | Love Song | Anne Murray | 0917 | ✅ |
| 502 | Love Train | The O'Jays | 0202 | ✅ |
| 503 | Lovely Day | Bill Withers | 0823 | ✅ |
| 504 | Lovers Who Wander | Dion | 1210 | ✅ |
| 505 | Lovin' You | Minnie Riperton | 1257 | ✅ |
| 506 | Loving Her Was Easier (Than Anything I'll Ever Do Again) | Kris Kristofferson | 1135 | ✅ |
| 507 | Lucille | Kenny Rogers | 0731 | ✅ |
| 508 | Lucky | Greg Kihn | 1027 | ✅ |
| 509 | Lucky Man | Emerson, Lake & Palmer | 1180 | ✅ |
| 510 | Lyin' Eyes | Eagles | 0296 | ✅ |
| 511 | Ma Belle Amie | The Tee Set | 0109 | ✅ |
| 512 | Maggie May | Rod Stewart | 0100 | ✅ |
| 513 | Magic Man | Heart | 0215 | ✅ |
| 514 | Magic Man | Heart | 0800 | ✅ |
| 515 | Make A Little Magic | Nitty Gritty Dirt Band | 0859 | ✅ |
| 516 | Make Me Smile | Chicago | 1085 | ✅ |
| 517 | Man In The Mirror | Michael Jackson | 1188 | ✅ |
| 518 | Maneater | Daryl Hall & John Oates | 0633 | ✅ |
| 519 | Maniac | Michael Sembello | 0553 | ✅ |
| 520 | Maybe I'm Amazed | Paul McCartney | 0206 | ✅ |
| 521 | Maybe Tomorrow | Badfinger | 0723 | ✅ |
| 522 | Me Myself And I | De La Soul | 0887 | ✅ |
| 523 | Mercy Mercy Me (The Ecology) | Marvin Gaye | 0819 | ✅ |
| 524 | Mighty Good Lovin' | The Miracles | 1134 | ✅ |
| 525 | Miss You | The Rolling Stones | 0958 | ✅ |
| 526 | Misunderstanding | Genesis | 0393 | ✅ |
| 527 | Modern Love | David Bowie | 0970 | ✅ |
| 528 | Money | Pink Floyd | 0269 | ✅ |
| 529 | Mony Mony | Tommy James | 0928 | ✅ |
| 530 | Motownphilly | Boyz II Men | 0097 | ✅ |
| 531 | Mr. Bojangles | Jerry Jeff Walker | 0294 | ✅ |
| 532 | Mrs. Robinson | Simon & Garfunkel | 0616 | ✅ |
| 533 | Must Of Got Lost | The J. Geils Band | 1069 | ✅ |
| 534 | My Boy | Elvis Presley | 0326 | ✅ |
| 535 | My Hometown | Bruce Springsteen | 1066 | ✅ |
| 536 | My Kinda Lover | Billy Squier | 1051 | ✅ |
| 537 | My Love | Paul McCartney | 1163 | ✅ |
| 538 | My Thang | James Brown | 0490 | ✅ |
| 539 | My Way | Elvis Presley | 0793 | ✅ |
| 540 | My Wish Came True | Elvis Presley | 1055 | ✅ |
| 541 | My World Fell Down | Sagittarius | 1182 | ✅ |
| 542 | Need You Tonight | INXS | 0687 | ✅ |
| 543 | Never Can Say Goodbye | Gloria Gaynor | 0190 | ✅ |
| 544 | Never Can Say Goodbye | Gloria Gaynor | 1068 | ✅ |
| 545 | Never Knew Love Like This Before | Stephanie Mills | 1112 | ✅ |
| 546 | Never My Love | The 5th Dimension | 0022 | ✅ |
| 547 | Nick Of Time | Bonnie Raitt | 0627 | ✅ |
| 548 | Night Moves | Bob Seger | 1171 | ✅ |
| 549 | Nightshift | Commodores | 0992 | ✅ |
| 550 | No Charge | Melba Montgomery | 0167 | ✅ |
| 551 | Not Fade Away | The Rolling Stones | 0457 | ✅ |
| 552 | Nowhere To Run | Martha & The Vandellas | 0074 | ✅ |
| 553 | Ob-La-Di, Ob-La-Da | The Beatles | 1107 | ✅ |
| 554 | Ode To Billie Joe | Bobbie Gentry | 1168 | ❌ Could not invert chord...inversion may not exist |
| 555 | Oh Father | Madonna | 1140 | ✅ |
| 556 | Oh Me Oh My (I'm A Fool For You Baby) | Aretha Franklin | 1042 | ✅ |
| 557 | Oh Me, Oh My (Dreams In My Arms) | Al Green | 0573 | ✅ |
| 558 | Oh My Angel | Bertha Tillman | 0511 | ✅ |
| 559 | Old Days | Chicago | 0445 | ✅ |
| 560 | Old Time Rock & Roll | Bob Seger | 0249 | ✅ |
| 561 | On And On And On | Abba | 0894 | ✅ |
| 562 | On Broadway | The Drifters | 0461 | ✅ |
| 563 | On Broadway | The Drifters | 0781 | ✅ |
| 564 | On The Road Again | Canned Heat | 0688 | ✅ |
| 565 | On The Wings Of A Nightingale | Everly Brothers | 0809 | ✅ |
| 566 | One | Metallica | 0884 | ✅ |
| 567 | One Bad Apple | The Osmonds | 0432 | ✅ |
| 568 | One Last Kiss | The J. Geils Band | 0478 | ✅ |
| 569 | One Less Bell To Answer | The 5th Dimension | 1127 | ✅ |
| 570 | One Night | Elvis Presley | 0399 | ✅ |
| 571 | One Way Or Another | Blondie | 0743 | ✅ |
| 572 | Only Sixteen | Dr. Hook | 1190 | ✅ |
| 573 | Out Of My Mind | Johnny Tillotson | 0638 | ✅ |
| 574 | Out Of Sight, Out Of Mind | Little Anthony & The Imperials | 0927 | ✅ |
| 575 | Over The Hills And Far Away | Led Zeppelin | 0053 | ✅ |
| 576 | Over The Hills And Far Away | Led Zeppelin | 1025 | ✅ |
| 577 | Paper Roses | Marie Osmond | 1245 | ✅ |
| 578 | Paradise By The Dashboard Light | Meat Loaf | 0071 | ✅ |
| 579 | Patches | Clarence Carter | 0276 | ✅ |
| 580 | People | Barbra Streisand | 0049 | ✅ |
| 581 | People Get Ready | Jeff Beck | 0698 | ✅ |
| 582 | People Got To Be Free | The Rascals | 0191 | ✅ |
| 583 | Perfidia | The Ventures | 0926 | ✅ |
| 584 | Philadelphia Freedom | Elton John | 0354 | ✅ |
| 585 | Pinball Wizard | The Who | 0421 | ✅ |
| 586 | Play That Funky Music | Wild Cherry | 1014 | ✅ |
| 587 | Press | Paul McCartney | 0772 | ✅ |
| 588 | Pressure | Billy Joel | 0205 | ✅ |
| 589 | Pretty In Pink | Psychedelic Furs | 0729 | ✅ |
| 590 | Private Dancer | Tina Turner | 0524 | ✅ |
| 591 | Private Dancer | Tina Turner | 1098 | ✅ |
| 592 | Private Dancer | Tina Turner | 1183 | ✅ |
| 593 | Promises | Eric Clapton | 0124 | ✅ |
| 594 | Promises | Eric Clapton | 0916 | ✅ |
| 595 | Promises In The Dark | Pat Benatar | 0227 | ✅ |
| 596 | Promises In The Dark | Pat Benatar | 0275 | ✅ |
| 597 | Put Your Hand In The Hand | Ocean | 0429 | ✅ |
| 598 | Quarter To Three | Gary U.S. Bonds | 0571 | ✅ |
| 599 | Queen Of Hearts | Juice Newton | 0690 | ✅ |
| 600 | Ramblin' Rose | Nat "King" Cole | 0220 | ✅ |
| 601 | Rebel Yell | Billy Idol | 1167 | ✅ |
| 602 | Red Red Wine | UB40 | 0083 | ✅ |
| 603 | Redneck Friend | Jackson Browne | 0545 | ✅ |
| 604 | Reelin' & Rockin' | Chuck Berry | 1110 | ✅ |
| 605 | Reminiscing | Little River Band | 0077 | ✅ |
| 606 | Rescue Me | Fontella Bass | 0777 | ✅ |
| 607 | Rhinestone Cowboy | Glen Campbell | 0246 | ✅ |
| 608 | Rich Girl | Daryl Hall & John Oates | 0485 | ✅ |
| 609 | Riders On The Storm | The Doors | 0945 | ✅ |
| 610 | Right Here, Right Now | Jesus Jones | 1169 | ✅ |
| 611 | Right Here, Right Now | Jesus Jones | 1260 | ✅ |
| 612 | Right Place Wrong Time | Dr. John | 0483 | ✅ |
| 613 | Rock 'N' Roll Fantasy | Bad Company | 0027 | ✅ |
| 614 | Rock And Roll Never Forgets | Bob Seger | 1071 | ✅ |
| 615 | Rock And Roll, Hoochie Koo | Rick Derringer | 1267 | ✅ |
| 616 | Rock This Town | Stray Cats | 1102 | ✅ |
| 617 | Rock This Town | Stray Cats | 1150 | ✅ |
| 618 | Rock'n Me | Steve Miller Band | 1249 | ✅ |
| 619 | Rocket Ride | Kiss | 0610 | ✅ |
| 620 | Rocky Mountain High | John Denver | 0720 | ✅ |
| 621 | Roll On Down The Highway | Bachman-Turner Overdrive | 0351 | ✅ |
| 622 | Ruby Baby | Dion | 0439 | ✅ |
| 623 | Runaround Sue | Dion | 0145 | ✅ |
| 624 | Running On Empty | Jackson Browne | 1155 | ✅ |
| 625 | Running Up That Hill | Kate Bush | 0531 | ✅ |
| 626 | Sad Eyes | Robert John | 1064 | ✅ |
| 627 | Sail On Sailor | The Beach Boys | 0239 | ✅ |
| 628 | San Franciscan Nights | The Animals | 0168 | ✅ |
| 629 | Sanctify Yourself | Simple Minds | 0254 | ✅ |
| 630 | Sara Smile | Daryl Hall & John Oates | 0708 | ✅ |
| 631 | Saturday Night | Bay City Rollers | 1228 | ✅ |
| 632 | Scarlet Fever | Kenny Rogers | 0372 | ✅ |
| 633 | School's Out | Alice Cooper | 0195 | ✅ |
| 634 | Sea Of Heartbreak | Don Gibson | 0169 | ✅ |
| 635 | Seasons Of The Heart | John Denver | 0463 | ✅ |
| 636 | Secret Love | Freddy Fender | 0872 | ✅ |
| 637 | See See Rider | LaVern Baker | 0425 | ✅ |
| 638 | September | Earth, Wind & Fire | 0804 | ✅ |
| 639 | Sexy Eyes | Dr. Hook | 0831 | ✅ |
| 640 | Shadow Dancing | Andy Gibb | 0193 | ✅ |
| 641 | Shadow Dancing | Andy Gibb | 0737 | ✅ |
| 642 | Shake Your Groove Thing | Peaches & Herb | 0550 | ✅ |
| 643 | Shape Of Things To Come | Max Frost & The Troopers | 0257 | ✅ |
| 644 | Shapes Of Things | The Yardbirds | 0990 | ✅ |
| 645 | She Bop | Cyndi Lauper | 0016 | ✅ |
| 646 | She Bop | Cyndi Lauper | 1274 | ✅ |
| 647 | She Thinks I Still Care | Elvis Presley | 0875 | ✅ |
| 648 | She's A Lady | Tom Jones | 0210 | ✅ |
| 649 | She's A Lady | Tom Jones | 0260 | ✅ |
| 650 | She's A Woman | The Beatles | 1193 | ✅ |
| 651 | Shock The Monkey | Peter Gabriel | 0092 | ✅ |
| 652 | Shock The Monkey | Peter Gabriel | 0141 | ✅ |
| 653 | Sidewalk Surfin' | Jan & Dean | 1272 | ✅ |
| 654 | Silent Lucidity | Queensryche | 0670 | ❌ Could not invert chord...inversion may not exist |
| 655 | Silent Lucidity | Queensryche | 0685 | ❌ Could not invert chord...inversion may not exist |
| 656 | Silent Night | Bing Crosby | 0123 | ✅ |
| 657 | Silver Threads And Golden Needles | The Cowsills | 0474 | ✅ |
| 658 | Situation | Yaz | 0594 | ✅ |
| 659 | Six Days On The Road | Dave Dudley | 0570 | ✅ |
| 660 | Sleep Walk | Santo & Johnny | 0157 | ✅ |
| 661 | Sleep Walk | Santo & Johnny | 0603 | ✅ |
| 662 | Smokin' In The Boy's Room | Brownsville Station | 0256 | ✅ |
| 663 | Smokin' In The Boy's Room | Brownsville Station | 0755 | ✅ |
| 664 | Smoking Gun | The Robert Cray Band | 0055 | ✅ |
| 665 | Smoking Gun | The Robert Cray Band | 0329 | ✅ |
| 666 | Some Days Are Diamonds (Some Days Are Stone) | John Denver | 0711 | ✅ |
| 667 | Some Like It Hot | The Power Station | 0044 | ✅ |
| 668 | Somebody s Watching Me | Rockwell | 0334 | ✅ |
| 669 | Somebody's Watching Me | Rockwell | 0882 | ✅ |
| 670 | Someone | The Rembrandts | 0414 | ✅ |
| 671 | Something About You | Level 42 | 0158 | ✅ |
| 672 | Something About You | Level 42 | 1237 | ✅ |
| 673 | Soul Dance Number Three | Wilson Pickett | 1021 | ✅ |
| 674 | Southern Cross | Crosby, Stills & Nash | 0589 | ✅ |
| 675 | Space Oddity | David Bowie | 0086 | ✅ |
| 676 | Spirits In The Material World | The Police | 0148 | ✅ |
| 677 | Stand By Me | David Ruffin,Jimmy Ruffin | 0119 | ✅ |
| 678 | Standing In The Shadows Of Love | Four Tops | 1192 | ✅ |
| 679 | Standing In The Shadows Of Love | Four Tops | 1283 | ✅ |
| 680 | Starting Over Again | Dolly Parton | 0944 | ✅ |
| 681 | Still | Commodores | 0507 | ✅ |
| 682 | Still Cruisin | The Beach Boys | 0228 | ✅ |
| 683 | Stoned Love | The Supremes | 0649 | ✅ |
| 684 | Stop The Wedding | Etta James | 0127 | ✅ |
| 685 | Stop This Game | Cheap Trick | 0539 | ✅ |
| 686 | Straight From The Heart | The Allman Brothers Band | 0798 | ✅ |
| 687 | Sugar Magnolia | Grateful Dead | 1034 | ✅ |
| 688 | Sugar Shack | The Fireballs | 0674 | ✅ |
| 689 | Suite: Judy Blue Eyes | Crosby, Stills & Nash | 0518 | ✅ |
| 690 | Sukiyaki | A Taste Of Honey | 1286 | ✅ |
| 691 | Summertime Blues | Blue Cheer | 1170 | ✅ |
| 692 | Sunday Morning Sunshine | Harry Chapin | 0412 | ✅ |
| 693 | Sunflower | Glen Campbell | 0347 | ✅ |
| 694 | Sunrise | Eric Carmen | 0655 | ✅ |
| 695 | Sunshine Of Your Love | Cream | 0114 | ✅ |
| 696 | Sunshine Superman | Donovan | 0383 | ✅ |
| 697 | Super Freak (Part I) | Rick James | 0812 | ✅ |
| 698 | Superman | Donna Fargo | 0358 | ✅ |
| 699 | Superman | Donna Fargo | 0874 | ✅ |
| 700 | Surfin' Safari | The Beach Boys | 0838 | ✅ |
| 701 | Surrender | Cheap Trick | 0555 | ✅ |
| 702 | Surrender | Cheap Trick | 1022 | ✅ |
| 703 | Sweet Caroline (Good Times Never Seemed So Good) | Bobby Womack | 0915 | ✅ |
| 704 | Sweet Home Alabama | Lynyrd Skynyrd | 0107 | ✅ |
| 705 | Sweet Little Rock And Roll | Chuck Berry | 0115 | ✅ |
| 706 | Sweet Love | Anita Baker | 0837 | ✅ |
| 707 | Sweet Music Man | Kenny Rogers | 0472 | ✅ |
| 708 | Sweet Nothin's | Brenda Lee | 0162 | ✅ |
| 709 | Sweet Soul Music | Arthur Conley | 0965 | ✅ |
| 710 | Sweet Surrender | Bread | 0847 | ✅ |
| 711 | Sweet Talkin' Guy | The Chiffons | 0026 | ✅ |
| 712 | Tainted Love | Soft Cell | 0654 | ✅ |
| 713 | Take A Chance On Me | Abba | 0961 | ✅ |
| 714 | Take Me Down | Alabama | 1082 | ✅ |
| 715 | Talk Back Trembling Lips | Johnny Tillotson | 1141 | ✅ |
| 716 | Talk To Me | Chico DeBarge | 0590 | ✅ |
| 717 | Tarzan Boy (From "Teenage Mutant Ninja Turtles III") | Baltimora | 0572 | ✅ |
| 718 | Tarzan Boy (From "Teenage Mutant Ninja Turtles III") | Baltimora | 0600 | ✅ |
| 719 | Teach Your Children | Crosby, Stills & Nash | 0905 | ✅ |
| 720 | Tell It Like It Is | Aaron Neville | 0691 | ✅ |
| 721 | Tell Me What You Want Me To Do | Tevin Campbell | 1145 | ✅ |
| 722 | Ten Percent | Double Exposure | 1164 | ✅ |
| 723 | Tenderness | General Public | 0389 | ❌ Could not invert chord...inversion may not exist |
| 724 | That Girl | Stevie Wonder | 0683 | ✅ |
| 725 | That Girl | Stevie Wonder | 0768 | ✅ |
| 726 | That Old Black Magic | Louis Prima & Keely Smith | 0746 | ✅ |
| 727 | That's Old Fashioned (That's The Way Love Should Be) | The Everly Brothers | 1248 | ✅ |
| 728 | That's The Way I Feel About Cha | Bobby Womack | 0297 | ✅ |
| 729 | The Anaheim, Azusa & Cucamonga Sewing Circle, Book Review And Timing Association | Jan & Dean | 0689 | ✅ |
| 730 | The Arms Of Orion | Prince (With Sheena Easton) | 1019 | ✅ |
| 731 | The Battle Of New Orleans | Johnny Horton | 0500 | ✅ |
| 732 | The Battle Of New Orleans | Johnny Horton | 0873 | ✅ |
| 733 | The Best | Tina Turner | 0348 | ✅ |
| 734 | The Best Disco In Town | The Ritchie Family | 0925 | ❌ Could not invert chord...inversion may not exist |
| 735 | The Bitch Is Back | Elton John | 0991 | ✅ |
| 736 | The Goonies R Good Enough | Cyndi Lauper | 0401 | ✅ |
| 737 | The Humpty Dance | Digital Underground | 0304 | ✅ |
| 738 | The Humpty Dance | Digital Underground | 0378 | ✅ |
| 739 | The Humpty Dance | Digital Underground | 0521 | ✅ |
| 740 | The Joker | Steve Miller Band | 0029 | ✅ |
| 741 | The Joker | Steve Miller Band | 0504 | ✅ |
| 742 | The Little Old Lady (From Pasadena) | Jan & Dean | 0635 | ✅ |
| 743 | The Long Run | Eagles | 0591 | ✅ |
| 744 | The Look | Roxette | 0567 | ✅ |
| 745 | The Look Of Love | Isaac Hayes | 0978 | ✅ |
| 746 | The Millionaire | Dr. Hook | 1009 | ✅ |
| 747 | The Night Chicago Died | Paper Lace | 0767 | ✅ |
| 748 | The Other Guy | Little River Band | 0310 | ✅ |
| 749 | The People In Me | The Music Machine | 0643 | ✅ |
| 750 | The Power | Snap | 0040 | ✅ |
| 751 | The Power | Snap | 0742 | ✅ |
| 752 | The Rose | Bette Midler | 0006 | ✅ |
| 753 | The Rose | Bette Midler | 1271 | ✅ |
| 754 | The Sounds Of Silence | Simon & Garfunkel | 1153 | ✅ |
| 755 | The Spirit Of Radio | Rush | 0105 | ✅ |
| 756 | The Stroke | Billy Squier | 0963 | ✅ |
| 757 | The Thrill Is Gone | B.B. King | 0605 | ✅ |
| 758 | The Twist | Chubby Checker | 0948 | ✅ |
| 759 | The Twist | Chubby Checker | 1103 | ✅ |
| 760 | The Way You Do The Things You Do | UB40 | 0139 | ✅ |
| 761 | The Way You Do The Things You Do | Rita Coolidge | 0291 | ✅ |
| 762 | The Way You Do The Things You Do | UB40 | 0885 | ✅ |
| 763 | The Ways Of A Woman In Love | Johnny Cash | 0787 | ✅ |
| 764 | The Year That Clayton Delaney Died | Tom T. Hall | 1194 | ✅ |
| 765 | Theme From Electric Surfboard | Brother Jack McDuff | 0251 | ✅ |
| 766 | Theme From The Dukes Of Hazzard (Good Ol' Boys) | Waylon Jennings | 0802 | ✅ |
| 767 | There But For Fortune | Joan Baez | 1087 | ✅ |
| 768 | There Goes My Everything | Elvis Presley | 0993 | ✅ |
| 769 | There She Goes | The La's | 1289 | ✅ |
| 770 | There'll Never Be | Switch | 1078 | ✅ |
| 771 | There's No Other (Like My Baby) | The Crystals | 1094 | ✅ |
| 772 | There's The Girl | Heart | 0281 | ✅ |
| 773 | There's The Girl | Heart | 0660 | ✅ |
| 774 | These Boots Are Made For Walkin' | Nancy Sinatra | 0284 | ✅ |
| 775 | Think | James Brown | 0640 | ✅ |
| 776 | Think Of Me | Buck Owens | 1154 | ✅ |
| 777 | This House | Tracie Spencer | 0530 | ✅ |
| 778 | This Little Girl | Dion | 1063 | ✅ |
| 779 | This Should Go On Forever | Rod Bernard | 0707 | ✅ |
| 780 | This Song | George Harrison | 0361 | ✅ |
| 781 | Those Lazy-Hazy-Crazy Days Of Summer | Nat "King" Cole | 0516 | ✅ |
| 782 | Those Lazy-Hazy-Crazy Days Of Summer | Nat "King" Cole | 1132 | ✅ |
| 783 | Three Hearts In A Tangle | Roy Drusky | 1006 | ✅ |
| 784 | Three Times A Lady | Commodores | 1201 | ✅ |
| 785 | Through The Years | Kenny Rogers | 0338 | ✅ |
| 786 | Through The Years | Kenny Rogers | 0832 | ✅ |
| 787 | Till The End Of The Day | The Kinks | 0904 | ✅ |
| 788 | Time For Me To Fly | REO Speedwagon | 0268 | ✅ |
| 789 | Time For Me To Fly | REO Speedwagon | 0910 | ✅ |
| 790 | Time Is On My Side | The Rolling Stones | 0387 | ✅ |
| 791 | Time Is On My Side | The Rolling Stones | 0597 | ✅ |
| 792 | Time Is On My Side | The Rolling Stones | 0780 | ✅ |
| 793 | Time Will Reveal | Debarge | 1013 | ✅ |
| 794 | Tonight, Tonight, Tonight | Genesis | 0236 | ✅ |
| 795 | Too Many Rivers | Brenda Lee | 0696 | ✅ |
| 796 | Too Weak To Fight | Clarence Carter | 0585 | ✅ |
| 797 | Too Weak To Fight | Clarence Carter | 0765 | ✅ |
| 798 | Torn Between Two Lovers | Mary MacGregor | 1138 | ✅ |
| 799 | Town Without Pity | Gene Pitney | 1037 | ✅ |
| 800 | Trampled Under Foot | Led Zeppelin | 0525 | ✅ |
| 801 | Treat Her Like A Lady | Cornelius Brothers & Sister Rose | 0932 | ✅ |
| 802 | Treat Her Like A Lady | Cornelius Brothers & Sister Rose | 1280 | ✅ |
| 803 | Treat Her Right | Roy Head | 1125 | ✅ |
| 804 | True | Spandau Ballet | 0091 | ✅ |
| 805 | True Colors | Cyndi Lauper | 0803 | ✅ |
| 806 | Tryin' To Live My Life Without You | Bob Seger | 0830 | ✅ |
| 807 | Tuff Enuff | The Fabulous Thunderbirds | 1062 | ✅ |
| 808 | Tumbling Dice | The Rolling Stones | 0130 | ✅ |
| 809 | Twilight Zone | Golden Earring | 0170 | ✅ |
| 810 | Twistin  The Night Away (From "Innerspace") | Rod Stewart | 0620 | ✅ |
| 811 | Two Hearts | Phil Collins | 0043 | ✅ |
| 812 | Unchained Melody | The Righteous Brothers | 0587 | ✅ |
| 813 | Unchained Melody | Righteous Brothers | 1007 | ✅ |
| 814 | Undercover Angel | Alan O'Day | 0367 | ✅ |
| 815 | Unforgettable | Dinah Washington | 0192 | ❌ Could not invert chord...inversion may not exist |
| 816 | Unforgettable | Natalie Cole | 0982 | ✅ |
| 817 | Unskinny Bop | Poison | 0810 | ✅ |
| 818 | Upside Down | Diana Ross | 1285 | ✅ |
| 819 | Venus | Bananarama | 0981 | ✅ |
| 820 | Waiting On A Friend | The Rolling Stones | 0278 | ✅ |
| 821 | Waiting On A Friend | The Rolling Stones | 0332 | ✅ |
| 822 | Wake Me Up Before You Go-Go | Wham! | 0542 | ✅ |
| 823 | Walk Like A Man | Grand Funk Railroad | 0762 | ✅ |
| 824 | Walk On The Wild Side (Part 1) | Jimmy Smith | 0455 | ✅ |
| 825 | Walk Right Back | The Everly Brothers | 0153 | ✅ |
| 826 | Walk Right In | The Moments | 0554 | ✅ |
| 827 | Walk Right In | Dr. Hook | 0761 | ✅ |
| 828 | Walk This Way | Run-D.M.C. | 0879 | ✅ |
| 829 | Walking In Memphis | Marc Cohn | 0775 | ✅ |
| 830 | Wanna Be Startin' Somethin' | Michael Jackson | 0223 | ✅ |
| 831 | War | Edwin Starr | 0893 | ✅ |
| 832 | We Are The Champions | Queen | 0588 | ✅ |
| 833 | We Don't Need Another Hero (Thunderdome) | Tina Turner | 1031 | ✅ |
| 834 | We Don't Talk Anymore | Cliff Richard | 1273 | ✅ |
| 835 | We Two | Little River Band | 0104 | ✅ |
| 836 | We're All Alone | Rita Coolidge | 0806 | ✅ |
| 837 | Wendy | The Beach Boys | 0479 | ✅ |
| 838 | What Have I Done To Deserve This? | Pet Shop Boys | 0648 | ✅ |
| 839 | What You Get Is What You See | Tina Turner | 1104 | ✅ |
| 840 | What's Love Got To Do With It | Tina Turner | 0150 | ✅ |
| 841 | Wheels | The String-A-Longs | 0147 | ✅ |
| 842 | Wheels | The String-A-Longs | 0318 | ✅ |
| 843 | Wheels | The String-A-Longs | 0863 | ✅ |
| 844 | When It's Love | Van Halen | 1281 | ✅ |
| 845 | When Will I Be Loved | Linda Ronstadt | 0324 | ✅ |
| 846 | When Will I Be Loved | Linda Ronstadt | 0839 | ✅ |
| 847 | Where Are You | Dinah Washington | 0722 | ✅ |
| 848 | Where Are You | Dinah Washington | 1099 | ✅ |
| 849 | Where Or When | Dion | 0434 | ✅ |
| 850 | Where Or When | Dion | 0816 | ✅ |
| 851 | Where The Streets Have No Name | Pet Shop Boys | 0382 | ✅ |
| 852 | Where The Streets Have No Name | Pet Shop Boys | 1300 | ✅ |
| 853 | White Christmas | Bing Crosby | 0241 | ✅ |
| 854 | White Wedding | Billy Idol | 0701 | ✅ |
| 855 | White Wedding | Billy Idol | 1296 | ✅ |
| 856 | Who Wears These Shoes? | Elton John | 1269 | ✅ |
| 857 | Who Will You Run To | Heart | 1089 | ✅ |
| 858 | Wichita Lineman | Glen Campbell | 1114 | ✅ |
| 859 | Wild Horses | The Rolling Stones | 0094 | ✅ |
| 860 | Wild Horses | Gino Vannelli | 0407 | ✅ |
| 861 | Will The Wolf Survive | Los Lobos | 1119 | ✅ |
| 862 | Will You Love Me Tomorrow | The Shirelles | 1239 | ✅ |
| 863 | Willie And The Hand Jive | Eric Clapton | 0194 | ✅ |
| 864 | Wish Someone Would Care | Irma Thomas | 0598 | ✅ |
| 865 | With A Little Help From My Friends | Joe Cocker | 0675 | ✅ |
| 866 | With A Little Luck | Paul McCartney | 0456 | ✅ |
| 867 | With Or Without You | U2 | 0681 | ✅ |
| 868 | With You I'm Born Again | Billy Preston | 0540 | ✅ |
| 869 | Woman To Woman | Shirley Brown | 0400 | ✅ |
| 870 | Wonderful World, Beautiful People | Jimmy Cliff | 0203 | ✅ |
| 871 | World In My Eyes | Depeche Mode | 0442 | ✅ |
| 872 | World In My Eyes | Depeche Mode | 0757 | ✅ |
| 873 | Worried Guy | Johnny Tillotson | 0267 | ✅ |
| 874 | Would It Make Any Difference To You | Etta James | 0726 | ✅ |
| 875 | Years From Now | Dr. Hook | 0656 | ✅ |
| 876 | You Can Call Me Al | Paul Simon | 0081 | ✅ |
| 877 | You Can Call Me Al | Paul Simon | 0833 | ✅ |
| 878 | You Can't Judge A Book By The Cover | Bo Diddley | 0179 | ✅ |
| 879 | You Can't Roller Skate In A Buffalo Herd | Roger Miller | 0308 | ✅ |
| 880 | You Can't Roller Skate In A Buffalo Herd | Roger Miller | 0669 | ✅ |
| 881 | You Decorated My Life | Kenny Rogers | 0238 | ✅ |
| 882 | You Don't Own Me | Lesley Gore | 1211 | ✅ |
| 883 | You Make Me Feel Like Dancing | Leo Sayer | 0986 | ✅ |
| 884 | You Took The Words Right Out Of My Mouth | Meat Loaf | 0807 | ✅ |
| 885 | You're The First, The Last, My Everything | Barry White | 0796 | ✅ |
| 886 | You've Got A Friend | Roberta Flack,Donny Hathaway | 0004 | ✅ |
| 887 | You've Got A Friend | Roberta Flack,Donny Hathaway | 1229 | ✅ |
| 888 | You've Got Another Thing Comin' | Judas Priest | 0861 | ✅ |
| 889 | Young Hearts Run Free | Candi Staton | 0390 | ✅ |
| 890 | Young Hearts Run Free | Candi Staton | 0522 | ✅ |
## Meta-Corpus (post-millennial diatonic chord-loop dataset)

[meta-corpus-complete-aggregate](https://www.kaggle.com/datasets/jpmusdata/meta-corpus-complete-aggregate) on Kaggle: 224 pop songs with harmonic analyses, featuring diatnoic chord loops from pop songs after 2000. 27 sample songs were expert-encoded into `.har` files (Clercq-Temperley notation, same format as the RS200 corpus above); the other 197 were converted from the CSV's scale-degree chord notation (e.g. `2-` for `ii`, `6o` for `viio`) into the same `.har` format via a Python script.

Imported into the app via:

```sh
python manage.py add_scores ../datasets/meta-pop-corpus har rs
```

### Conversion from the CSV

The converter preserves `$section*N` references rather than expanding them, matching how the hand-authored files themselves use these references (some sections are defined only as an alias for another, e.g. `Intro: $a*2`). It was validated against all 27 hand-authored files before running on the rest: the degree-to-Roman-numeral mapping was empirically confirmed against ~150 tokens harvested from those files, and the remaining logic (measure/bar handling, reference-vs-chord-line formatting, key derivation) was iterated until it matched musically, verified by round-tripping both the hand-authored and generated `.har` text through the actual `rs` parser and comparing the resulting chord progressions, not just comparing text.

162 of 197 songs converted successfully. The 34 that didn't are all genuine gaps or typos in the source CSV — a structure line or chord reference points to a section name that's never actually defined anywhere in that song's rows, or a required row is missing entirely.

### Import status

**184 of 224 songs imported successfully.** Of the 40 that didn't make it in:

- **34 songs** never got a `.har` file at all (see above).
- **6 songs** got a `.har` file (hand-authored or converted) but still failed the actual `rs` import — pre-existing issues in that file's content (an unparseable chord figure, a malformed reference like `$Ch*2n`, or a reference that can't be expanded), not something introduced by the conversion process.

| # | Song | Artist | Source | Status |
|---|---|---|---|---|
| 1 | 1-2 Step | CiaraÊ& Missy 'Misdemeanor' Elliot | hand-authored | ✅ |
| 2 | 21 Guns | Green Day | hand-authored | ✅ |
| 3 | 3 | Britney Spears | hand-authored | ❌ Invalid figure: R*4 |
| 4 | 33 "GOD" | Bon Iver | hand-authored | ✅ |
| 5 | 50 Ways to Say Goodbye | Train | hand-authored | ❌ No roman numeral found in '5' |
| 6 | A New Day Has Come | Celine Dion | hand-authored | ✅ |
| 7 | A Sky Full of Stars | Coldplay | auto-converted | ✅ |
| 8 | A Thousand Miles | Vanessa Carlton | hand-authored | ❌ Invalid figure: viio. |
| 9 | a_sky_full_of_stars.har |  | hand-authored (no CSV entry) | ❌ Invalid figure: IV. |
| 10 | According to You | Orianthi | hand-authored | ✅ |
| 11 | Adore You | Miley Cyrus | auto-converted | ✅ |
| 12 | Again | Lenny Kravitz | auto-converted | ✅ |
| 13 | Ain't It Funny | Jennifer Lopez & Ja Rule | auto-converted | ✅ |
| 14 | Alejandro | Lady Gaga | auto-converted | ✅ |
| 15 | All About That Bass | Meghan Trainor | auto-converted | ✅ |
| 16 | All For You | Janet Jackson | auto-converted | ✅ |
| 17 | All Night | Icona Pop | auto-converted | ✅ |
| 18 | All of Me | John Legend | auto-converted | ✅ |
| 19 | All You Wanted | Michelle Branch | auto-converted | ✅ |
| 20 | Already Gone | Kelly Clarkson | auto-converted | ✅ |
| 21 | Always | Erasure | auto-converted | ✅ |
| 22 | Always On Time | Ja Rule & Ashanti | auto-converted | ✅ |
| 23 | American Kids | Kenny Chesney | auto-converted | ❌ not converted |
| 24 | American Oxygen | Rihanna | auto-converted | ❌ not converted |
| 25 | Amnesia | 5 Seconds of Summer | auto-converted | ✅ |
| 26 | Angel | Shaggy | auto-converted | ✅ |
| 27 | Apologize | Timbaland feat. OneRepublic | auto-converted | ✅ |
| 28 | Back Here | BBMak | auto-converted | ❌ not converted |
| 29 | Back to December | Taylor Swift | auto-converted | ❌ not converted |
| 30 | Back Together | Robin Thicke featuring Nicky Minaj | auto-converted | ✅ |
| 31 | Bad Blood | Taylor Swift feat. Kendrick Lamar | auto-converted | ✅ |
| 32 | Bad Guy | Billie Eillish | auto-converted | ❌ Cannot expand rule Chn in <music21.romanText.clercqTemperley.CTRule text='S: $In $Vr $PCh $drop $Ch $Vr_b $PCh $Ch*2n $outro'> |
| 33 | Bad Romance | Lady Gaga | auto-converted | ✅ |
| 34 | Bailando | Enrique Iglesias feat. Descemer Bueno and Gente de Zona | auto-converted | ✅ |
| 35 | Bartender | Lady Antebellum | auto-converted | ✅ |
| 36 | Battlefield | Jordin Sparks | auto-converted | ❌ not converted |
| 37 | Be Like That | 3 Doors Down | auto-converted | ❌ not converted |
| 38 | Be There | Krewella | auto-converted | ✅ |
| 39 | Beautiful | Akon feat. Colby O'Donis and Kardinal Offishall | auto-converted | ✅ |
| 40 | Beauty and a Beat | Justin Bieber featuring Nicki Minaj | auto-converted | ✅ |
| 41 | Behind These Hazel Eyes | Kelly Clarkson | auto-converted | ✅ |
| 42 | Best I ever Had | Drake | auto-converted | ✅ |
| 43 | Better in Time | Leona Lewis | auto-converted | ✅ |
| 44 | Better Now | Post Malone | auto-converted | ✅ |
| 45 | Beyond | Daft Punk | auto-converted | ❌ not converted |
| 46 | Big Girls Don't Cry | Fergie | auto-converted | ✅ |
| 47 | Bitch | Merridith Brooks | auto-converted | ❌ not converted |
| 48 | Bitch, Don't Kill My Vibe | Kendrick Lamar | auto-converted | ✅ |
| 49 | Blank Space | Taylor Swift | auto-converted | ✅ |
| 50 | Bleeding Love | Leona Lewis | auto-converted | ✅ |
| 51 | Blow Me (One Last Kiss) | P!nk | auto-converted | ✅ |
| 52 | Blurred Lines | Robin Thicke, T.I. &Â Pharrell Williams | auto-converted | ✅ |
| 53 | Blurry | Puddle of Mudd | auto-converted | ✅ |
| 54 | Body | Loud Luxury ft. Brando | auto-converted | ✅ |
| 55 | Body Party | Ciara | auto-converted | ✅ |
| 56 | Boulevard of Broken Dreams | Green Day | auto-converted | ✅ |
| 57 | Boyfriend | Justin Bieber | auto-converted | ✅ |
| 58 | Break a Sweat | Becky G. | auto-converted | ✅ |
| 59 | Break Free | Ariana Grande | auto-converted | ❌ not converted |
| 60 | Break Your Heart | Taio Cruz feat. Ludacris | auto-converted | ✅ |
| 61 | Breakaway | Kelly Clarkson | auto-converted | ✅ |
| 62 | Breakeven | The Script | auto-converted | ❌ not converted |
| 63 | Breathe | Faith Hill | auto-converted | ✅ |
| 64 | Bring Me To Life | Evanescence& Paul McCoy | auto-converted | ✅ |
| 65 | Building a Mystery | Sarah McLachlan | auto-converted | ✅ |
| 66 | Burn | Ellie Goulding | hand-authored | ✅ |
| 67 | Burn | Usher | auto-converted | ❌ not converted |
| 68 | Burnin' It Down | Jason Aldean | auto-converted | ✅ |
| 69 | Cake | Flo Rida and 99 Percent | auto-converted | ✅ |
| 70 | California Gurls | Katy Perry featuring Snoop Dog | auto-converted | ✅ |
| 71 | Call Me Maybe | Carly Rae Jepsen | auto-converted | ✅ |
| 72 | Can't Get You Out Of My Head | Kylie Minogue | auto-converted | ✅ |
| 73 | Can't Stop Dancing | Becky G. | auto-converted | ❌ not converted |
| 74 | Can't Stop The Feeling | Justin Timberlake | auto-converted | ✅ |
| 75 | Case Of The Ex (Whatcha Gonna Do) | M_a | auto-converted | ✅ |
| 76 | Chandelier | Sia | hand-authored | ✅ |
| 77 | Chariot | Gavin DeGraw | auto-converted | ❌ not converted |
| 78 | Chasing Cars | Snow Patrol | auto-converted | ❌ not converted |
| 79 | Cheap Thrills | Sia feat. Sean Paul | auto-converted | ✅ |
| 80 | Cheerleader | OMI | auto-converted | ✅ |
| 81 | Circles | Post Malone | auto-converted | ✅ |
| 82 | Claudia Lewis | M83 | auto-converted | ✅ |
| 83 | Closer | The Chainsmokers ft. Halsey | auto-converted | ❌ not converted |
| 84 | Collide | Howie Day | auto-converted | ✅ |
| 85 | Come Over | Kenny Chesney | auto-converted | ❌ not converted |
| 86 | Complicated | Avril Lavigne | auto-converted | ❌ not converted |
| 87 | Contact | Daft Punk | auto-converted | ✅ |
| 88 | Cool for the Summer | Demi Lovato | auto-converted | ✅ |
| 89 | Cool Kids | Echosmith | auto-converted | ❌ not converted |
| 90 | Counting Stars | OneRepublic | auto-converted | ✅ |
| 91 | Crash and Burn | Savage Garden | auto-converted | ✅ |
| 92 | Crash My Party | Luke Bryan | auto-converted | ✅ |
| 93 | Crazy | Gnarls Barkley | auto-converted | ❌ not converted |
| 94 | Crazy Girl | Eli Young Band | auto-converted | ✅ |
| 95 | Crazy In Love | BeyoncŽ & Jay-Z | auto-converted | ✅ |
| 96 | Cruise | Florida Georgia Line feat. Nelly | auto-converted | ✅ |
| 97 | Dance Monkey | Tones And I | auto-converted | ❌ not converted |
| 98 | Dancing With a Stranger | Sam Smith & Normami | auto-converted | ✅ |
| 99 | Dangerous Woman | Ariana Grande | auto-converted | ✅ |
| 100 | Daylight | Maroon 5 | auto-converted | ✅ |
| 101 | Demons | Imagine Dragons | auto-converted | ✅ |
| 102 | Despacito | Luis Fonsi & Daddy Yankee | auto-converted | ✅ |
| 103 | Dilemma | Nelly & Kelly Rowland | auto-converted | ✅ |
| 104 | Dirty Little Secret | The All-American Rejects | auto-converted | ✅ |
| 105 | DJ Got Us Falling In Love Again | Usher | auto-converted | ✅ |
| 106 | Doin' It Right | Daft Punk | auto-converted | ❌ not converted |
| 107 | Don't Cha | The Pussycat Dolls | auto-converted | ✅ |
| 108 | Don't Forget Me | Red Hot Chili Peppers | auto-converted | ✅ |
| 109 | Don't Leave Me Alone | David Guetta featuring Anne-Marie | auto-converted | ✅ |
| 110 | Don't Let Me Down | The Chainsmokers feat. Daya | auto-converted | ✅ |
| 111 | Don't Matter | Akon | auto-converted | ✅ |
| 112 | Don't Stop The Music | Rihanna | auto-converted | ✅ |
| 113 | Don't Tell Me | Avril Lavigne | auto-converted | ✅ |
| 114 | Don't Trust Me | 3OH!3 | auto-converted | ✅ |
| 115 | Down | Jay Sean feat. Lil Wayne | auto-converted | ✅ |
| 116 | Drive By | Train | auto-converted | ✅ |
| 117 | Drops Of Jupiter (Tell Me) | Train | auto-converted | ✅ |
| 118 | Drunk on You | Luke Bryan | auto-converted | ✅ |
| 119 | Dynamite | Taio Cruz | auto-converted | ✅ |
| 120 | E.T. | Katy Perry | hand-authored | ✅ |
| 121 | Earned It | The Weeknd | auto-converted | ✅ |
| 122 | Eastside | Benny Blanco, with Halsey & Khalid | auto-converted | ✅ |
| 123 | Eenie Meenie | Sean Kingston and Justin Bieber | auto-converted | ✅ |
| 124 | El perdon (forgiveness) |  | hand-authored (no CSV entry) | ✅ |
| 125 | El perd—n (Forgiveness) | Nicky Jam and Enrique IglesiasÂ | auto-converted | ✅ |
| 126 | Elastic Heart | Sia | auto-converted | ✅ |
| 127 | Everything You Want | Vertical Horizon | auto-converted | ✅ |
| 128 | Face Down | The Red Jumpsuit Apparatus | auto-converted | ✅ |
| 129 | Fall for You | Secondhand Serenade | auto-converted | ✅ |
| 130 | Fallin' | Alicia Keys | auto-converted | ✅ |
| 131 | Family Affair | Mary J Blige | auto-converted | ❌ not converted |
| 132 | Feel Good Inc | Gorillaz | auto-converted | ✅ |
| 133 | Feels Like Tonight | Daughtry | auto-converted | ❌ not converted |
| 134 | Fight Song | Rachel Platten | auto-converted | ✅ |
| 135 | Firework | Katy Perry | auto-converted | ✅ |
| 136 | Fly Over States | Jason Aldean | auto-converted | ✅ |
| 137 | Follow Me | Uncle Kracker | auto-converted | ❌ not converted |
| 138 | Foolish Games | Jewel | auto-converted | ✅ |
| 139 | For the First Time | The Script | auto-converted | ✅ |
| 140 | Fortress | Bloc Party | auto-converted | ❌ not converted |
| 141 | Fragments of Time | Daft Punk | auto-converted | ✅ |
| 142 | Fuck It (I Don't Want You Back) | Eamon | auto-converted | ✅ |
| 143 | Fuckin' Perfect | P!nk | auto-converted | ✅ |
| 144 | Fuckin' Problems | ASAP Rocky feat. Drake, 2 Chainz, and Kendrick Lamar | auto-converted | ❌ not converted |
| 145 | Get Lucky | Daft Punk | hand-authored | ✅ |
| 146 | Get The Party Started | P!nk | auto-converted | ❌ not converted |
| 147 | Get Your Shine On | Florida Georgia Line | auto-converted | ✅ |
| 148 | Giorgio by Moroder | Daft Punk | auto-converted | ✅ |
| 149 | Girl Crush | Little Big Town | auto-converted | ✅ |
| 150 | Girlfriend | Avril Lavigne | auto-converted | ❌ not converted |
| 151 | Girls Like You | Maroon 5 & Cardi B | auto-converted | ✅ |
| 152 | Give Life Back to Music | Daft Punk | auto-converted | ✅ |
| 153 | Give Me Everything | Pitbull feat. NeYo, Afrojack, and Nayer | auto-converted | ✅ |
| 154 | Gives You Hell | The All-American Rejects | auto-converted | ✅ |
| 155 | God Gave Me You | Blake Shelton | auto-converted | ✅ |
| 156 | Gone, Gone, Gone | Phillip Phillips | auto-converted | ✅ |
| 157 | Heal Me | Lady Gaga | hand-authored | ✅ |
| 158 | Heart Attack | Demi Lovato | hand-authored | ✅ |
| 159 | Here Without You | Three Doors Down | auto-converted | ✅ |
| 160 | Heroes (We Could Be) | Alesso featuring Tove Lo | auto-converted | ✅ |
| 161 | Hey Mama | David Guetta featuring Nicki Minaj | hand-authored | ✅ |
| 162 | Honest | The Chainsmokers | auto-converted | ✅ |
| 163 | Hot 'n' cold | Katy Perry | hand-authored | ✅ |
| 164 | Hurts So Good | Astrid S | auto-converted | ❌ not converted |
| 165 | I Don't Care | Ed Sheeran & Justin Bieber | auto-converted | ✅ |
| 166 | I Gotta Feeling | The Black Eyed Peas | auto-converted | ✅ |
| 167 | I Kissed A Girl | Katy Perry | auto-converted | ✅ |
| 168 | I Knew You Were Trouble | Taylor Swift | auto-converted | ✅ |
| 169 | I'll Show You | Justin Bieber | auto-converted | ❌ not converted |
| 170 | Icey | Young Thug | auto-converted | ✅ |
| 171 | Instant Crush | Daft Punk | hand-authored | ✅ |
| 172 | It's a Slime | Young Thug & Lil' Uzi Vert | auto-converted | ✅ |
| 173 | It's Been Awhile | Staind | auto-converted | ✅ |
| 174 | Lean On | Major Lazer and DJ Snake | auto-converted | ✅ |
| 175 | Livewire | Oh Wonder | auto-converted | ✅ |
| 176 | Lose Yourself to Dance | Daft Punk | auto-converted | ✅ |
| 177 | Love Me Harder | Ariana Grande featuring The Weeknd | hand-authored | ✅ |
| 178 | Love Yourself | Justin Bieber | auto-converted | ❌ not converted |
| 179 | Midnight City | M83 | auto-converted | ✅ |
| 180 | Mine | Taylor Swift | auto-converted | ✅ |
| 181 | Motherboard | Daft Punk | auto-converted | ✅ |
| 182 | Night Sky | CHVRCHES | auto-converted | ✅ |
| 183 | Nights Like This | Kehlani ft. Ty Dolla $ign | auto-converted | ✅ |
| 184 | Out of the Woods | Taylor Swift | auto-converted | ✅ |
| 185 | Paris | The Chainsmokers | auto-converted | ✅ |
| 186 | Party Rock Anthem | LMFAO | auto-converted | ✅ |
| 187 | Perfect | Ed Sheeran | hand-authored | ❌ Cannot expand rule Vr in <music21.romanText.clercqTemperley.CTRule text='S: [Ab] $In*2 $Vr1*2 $Vr2 $Vr1 $Ch*4 $link $Vr*2 $Ch*4 $instr $Ch*4 $PostCh $outro'> |
| 188 | Perth | Bon Iver | auto-converted | ✅ |
| 189 | Photograph | Ed Sheeran | auto-converted | ✅ |
| 190 | Pillow Talk | ZAYN | auto-converted | ❌ not converted |
| 191 | Pour it Up | Rihanna | auto-converted | ✅ |
| 192 | Problem | Ariana Grande featuring Iggy Azalea | auto-converted | ❌ not converted |
| 193 | Radioactive | Imagine Dragons | auto-converted | ✅ |
| 194 | Red Dirt Road | Brooks and Dunn | auto-converted | ✅ |
| 195 | Representin' | Ludacris featuring Kelly Rowland | auto-converted | ✅ |
| 196 | Roar | Katy Perry | auto-converted | ✅ |
| 197 | Roses | The Chainsmokers featuring Rosez | auto-converted | ✅ |
| 198 | Royals | Lorde | auto-converted | ✅ |
| 199 | Same Old Love | Selena Gomez | hand-authored | ✅ |
| 200 | Secrets | The Weeknd | hand-authored | ✅ |
| 201 | Secrets | OneRepublic | hand-authored | ✅ |
| 202 | See You Again | Miley Cyrus | hand-authored | ✅ |
| 203 | Self Esteem | The Offspring | hand-authored | ✅ |
| 204 | Shake it Off | Taylor Swift | hand-authored | ✅ |
| 205 | Shape Of You | Ed Sheeran | auto-converted | ✅ |
| 206 | Something Just Like This | The Chainsmokers & Coldplay | auto-converted | ✅ |
| 207 | Sorry | Justin Bieber | auto-converted | ✅ |
| 208 | Stardust | çsgeir | auto-converted | ✅ |
| 209 | Style | Taylor Swift | auto-converted | ✅ |
| 210 | Talking Body | Tove Lo | auto-converted | ✅ |
| 211 | Teenage Dream | Katy Perry | auto-converted | ✅ |
| 212 | The Game of Love | Daft Punk | auto-converted | ✅ |
| 213 | The Night is Still Young | Nicki Minaj | auto-converted | ✅ |
| 214 | Tornado | J—nsi | auto-converted | ✅ |
| 215 | Touch | Daft Punk | auto-converted | ✅ |
| 216 | Unconditionally | Katy Perry | auto-converted | ✅ |
| 217 | Viva la Vida | Coldplay | auto-converted | ✅ |
| 218 | Want to Want Me | Jason Derulo | auto-converted | ✅ |
| 219 | We Are Never Ever Getting Back Together | Taylor Swift | auto-converted | ✅ |
| 220 | We Can't Stop | Miley Cyrus | auto-converted | ❌ not converted |
| 221 | What do You Mean | Justin Bieber | auto-converted | ✅ |
| 222 | Where are Ãœ Now | Skrillex, Diplo, & Justin Biber | auto-converted | ✅ |
| 223 | Within | Daft Punk | auto-converted | ✅ |
| 224 | Wrecking Ball | Miley Cyrus | auto-converted | ✅ |
