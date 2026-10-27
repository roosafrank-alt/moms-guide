# Monday update runbook (for the scheduled task)

Goal: keep Mom's Guide current AND keep finding new things for her. Mom lives in Wurtsboro NY 12790. She crochets and knits, gardens and walks, wants to meet friends and build a weekly routine, and dislikes anything branded "senior". Keep everything within about 45 minutes' drive (up to ~50 minutes is fine for a strong fit, as the guide already does for Roscoe, Warwick and Narrowsburg). Write in plain, short words.

Live site: https://roosafrank-alt.github.io/moms-guide/ (GitHub Pages, branch main). A printed binder (56 pages) was made on Oct 20, 2026; the user can reprint single pages.

The user's standing order (Oct 24 and Oct 26, 2026): check EVERY possible source each week, not just a short list. On Oct 26, 2026 a full six-lane search found about 120 verified new items that the Monday run had missed. Every Monday run must now be that thorough. A run that adds nothing is a sign the search was too shallow, not that nothing exists.

## Files
- `source/packet.html` is the master. Everything is data inside one JS file: `DAYS` (Mon to Sun items made with `I(name, time, where, drive, cost, phone, badge, note)`), `REC` (recurrence pill per item, matched BY POSITION to the items in each weekday, so if you add or remove a day item you must add or remove the matching entry in `REC[day]`), events with `EV(date, name, time, where, drive, cost, phone, last, note)`, fitness `F(...)`, volunteering `V(...)`, `TABS`, and the tables.
- `REC` labels: `['w', 'Every Thu', short]` weekly; `['m', 'Mondays Nov 2 to Dec 28', short]` weekly with a start/end (the app reads "Mon D to Mon D" from the label, so always write the start date when it is in the future); `['d', 'Nov 14, Dec 12 (2nd Sat)', short]` set dates only (write every date, the app reads them); `['q', 'Ask how often', short]` unknown.
- `EV` dates the app understands: `Sat Nov 7`, `Sat Nov 14 and Sat Dec 12`, `Sat Nov 7, 14, 28, Dec 5`, `Thursdays Nov 5 to Nov 19` (weekly series), `Weekends to Dec 20`, `Daily to Dec 31`. All EV items (except the farmers market pages) are merged into one date-ordered list, so it does not matter which events page you add them to.
- `source/ideas_data.py` holds the Ideas and Walks tabs (ARTS, GARD, HIKE, GROUP, RACES). RACES rows are (date, name, address, details, cost, contact); keep RACES in date order. `build_ideas.py` regenerates those tabs inside packet.html. Never edit the block between `// IDEAS BEGIN` and `// IDEAS END` in packet.html by hand.
- `UPDATES` (search "UPDATE LOG") feeds the "Recently updated" box and the "Last updated" date.
- `ADDED` (search "RECENTLY ADDED", just below UPDATES) feeds the phone app's "Recently added" section and the orange "New" tags. Each Monday, put one new entry at the TOP: `['YYYY-MM-DD', ['exact listing name', ...]]`. Use the exact name text you gave the listing (the first argument of `I`, the second of `EV`, the first of `V`/`F`, the first column of ideas rows, the name of a RACES row). Items stay "New" for 21 days. Trim entries older than about 2 months.
- The phone app also has "Interested" / "Not for me" buttons and a "Picked for you" box. Mom's choices are saved only on her phone. Do not change that code; it is not part of the data.
- `source/build_site.py` builds index.html, the PDF and the service-worker cache. It runs the checks and stops with an error if anything is wrong.

## Each Monday
1. Set today's date from the system. Remove events whose last date has passed. Remove past rows from RACES. Weekly items stay unless the source says they ended. Update "through <date>" notes that have passed.
2. Search. Run the SIX LANES below. If the Agent tool is available, run them as six parallel research agents, each given its lane's section of this file, the dedupe rule and the verification rule, and told to return its findings as text (subagents cannot write report files). If not, do the lanes one after another. Give each lane real effort; the Oct 26 lanes each took 20 to 50 minutes. Every lane must:
   - read `source/packet.html` and `source/ideas_data.py` first and skip anything already listed (dedupe);
   - check every source in its list, then search the web broadly for more (add new good sources to this file);
   - verify each item on an official page (organizer, library, town, park or ticket page) and give the URL;
   - list the sources it could not open, so the summary never claims they were checked.
3. Add only things verified on an official page. Badge `'c'` (dates confirmed) when the page shows the date, `'a'` (call first) when something important is missing or conflicting. Never invent dates, prices, phone numbers or addresses. Leave out or mark "call first" anything you cannot verify. Skip anything branded "senior" (or describe the activity without that word if the activity itself is open to all ages, as with Bone Builders).
4. Open items to chase: Encore spring 2027 (catalog expected January), First Day Hikes Jan 1 2027 locations (mid-December), Delaware Highlands 2027 eagle bus tour dates, MEEC SnO&W snowshoe walk 2027 date (January), Sullivan SWCD tree sale (January), Liberty Kindred Stitchers end date, Grumpy Goat "Slow Down Sunday" dates, Hidden Charm studio town, HPAC line dancing winter dates, Country Quilters Guild (Pine Bush) current info, Goshen Crochetiers Dec 15 series, Walden library November calendar, Narrowsburg Holiday Market 2026, Wallkill River Center "Handmade for the Holidays" date (Nov 12 or Dec 12), Bethel Woods Peace Love and Lights price ($12 vs $27).
5. Add entries at the TOP of `UPDATES`: `{ d: 'YYYY-MM-DD', t: 'short plain text', k: 'ev' }` where `k` is a tab key (`mon`..`sun`, `ev`, `walk`, `enc`, `fit`, `vol`, `ideas`, `me`, `host`, `plan`) or `'my'`. Only real additions, changes and removals Mom would care about. Add the new names to `ADDED` (see Files).
6. Run `python3 source/build_site.py`. If it fails, fix the cause or revert your edits. Do not publish a broken build.
7. Commit all changes (index.html, sw.js, Moms_Activity_Packet.pdf, source/*) with a clear message and push to `main`.
8. Message the user a short summary: how many items were added (with the 3 best), removed or changed, what could not be verified, and which sources could not be opened.

## The six lanes and their sources (all checked Oct 26, 2026)

### Lane 1: Libraries (adult programs: fiber and craft groups, games, book and writing groups, talks, exercise, tech help, film, music)
Read each library's own calendar. LibCal calendars (`<name>.libcal.com`) often need JavaScript: if the calendar page shows no events, open single event pages (`<name>.libcal.com/event/<id>`, which WebFetch can read), try the list view `https://<name>.libcal.com/calendar?cid=-1&t=d&d=0000-00-00&cal=-1&inc=0&audience=adult&view=list`, or search the web for the program name plus the library. If a browser tool is available, use it.
- Mamakating (Wurtsboro): calendar.mamakatinglibrary.org, registrations at mamakatinglibrary.org/registrations, 845-888-8004
- Crawford (Monticello): ebcpl.libcal.com, 845-794-4660
- Liberty: libertypubliclibrary.libcal.com, 845-292-6070
- Thrall (Middletown): thrall.libcal.com, 845-341-5454
- Ellenville: eplm.org/calendar-2, 845-647-5530
- Port Jervis: portjervislibrary.org/pages/index/228856/calendar-of-events (List View), 845-856-7313
- Rosendale: rosendalelibrary.libcal.com, 845-658-9013
- Wallkill: wallkillpubliclibrary.libcal.com, 845-895-3707
- Goshen: goshenpubliclibrary.libcal.com, 845-294-6606
- Florida NY: floridapl.librarycalendar.com, 845-651-7659
- Woodbury / Highland Mills: woodburypubliclibrary.libcal.com, 845-928-6162
- Elting (New Paltz): eltinglibrary.libcal.com, 845-255-5030
- Moffat (Washingtonville): moffat.librarycalendar.com, 845-496-5483
- Western Sullivan (Narrowsburg, Jeffersonville, Callicoon): wsplonline.libcal.com (NOT wspl.org, a different library)
- Albert Wisner (Warwick): albertwisnerlibrary.org/events, 845-986-1047
- Newburgh Free Library: newburghlibrary.libcal.com (edge of range)
- Walden (Josephine-Louise): waldenpubliclibrary.org (monthly calendar is an image; read it as an image)
- Pike County PA (Milford, Dingman): pikecountypubliclibrary.com/events, 570-296-8211
- Livingston Manor and Roscoe: 845-439-5440 / 607-498-5574
- Monroe: monroefreelibrary.org/Events (scripted; only page 1 was readable)
- Pine Bush (pinebusharealibrary.org; robots-blocked, titles only), Montgomery, Fallsburg, Chester: had nothing useful on Oct 26; recheck monthly.

### Lane 2: Fiber arts and crafts (crochet, knitting, spinning, weaving, quilting, sewing, embroidery, holiday craft fairs)
- Yarn shops: Grumpy Goat Fine Yarn, Port Jervis (grumpygoatfineyarn.com/products/classes); Knit One Needlepoint Too, Monticello (needlepointtoo.net); Fiber on Main, Hurleyville (fiberonmain.com/calendar); Wool Worth, Callicoon (wool-worth.com/events-classes; far); Cornwall Yarn Shop (far)
- Studios: Hudson Valley Atelier, Florida NY (hudsonvalleyatelier.com/calendar); Wallkill River Center for the Arts (wallkill.art/events); Wurtsboro Art Alliance (waagallery.org, classes page and calendar; event pop-ups need a browser); Unison Arts (unisonarts.org); Catskill Weaving School, Kingston (far)
- Guilds and groups: Calico Geese Quilting Guild (sullivancce.org/home-family/calico-geese-quilting-guild); Country Quilters Guild, Pine Bush; Warwick Valley Quilters' Guild (warwickvalleyqg.org); quiltguilds.com/new-york-quilt-guilds (user-submitted leads only); Project Linus OC/PC (projectlinusocpc.org); MEEC Sky Stitching (mamakating.gov calendar)
- Fiber farms: NY Fiber Trail directory (nyfibertrail.com), Buck Brook Alpacas (Roscoe), Will-O-Wool (Callicoon), Tuveemor Alpacas (Wurtsboro; site robots-blocked)
- Holiday markets and fairs: Port Jervis Christkindlmarkt (portjervisny.gov/events, poster image), Tri-State Mercantile (tristatemercantile.com/upcoming-events-workshops), Valley Central Holiday Craft Fair (vcsc1964.org/events.html), SUNY Sullivan Holiday Craft Fair, New Century Christmas Market (newcenturyfestivals.com), Narrowsburg Union Holiday Market (narrowsburgunion.com/holiday-market), MEEC Holiday Artisan Market, Unison Craft Fair, Farmhouse Project Makers Market (Callicoon)
- Search: church, school and fire department bazaars (they post in November), Meetup fiber groups, Ravelry local groups.

### Lane 3: Gardening, farms, markets, food
- Cornell Cooperative Extension Orange: cceorangecounty.org/events (workshops, gardening classes, Big Glean, volunteer orientation), Master Gardener blog (blogs.cornell.edu/master-gardeners-cce-oc)
- Cornell Cooperative Extension Sullivan: sullivancce.org/events (WebFetch is blocked; read it with a browser or via the Sullivan Catskills calendar), registration pub.cce.cornell.edu/event_registration/main/events.cfm?dept=248
- CCE Ulster: cce.cornell.edu/ulster/events (Master Gardener winter lectures Feb to Mar)
- Sullivan County Soil and Water tree sale: sullivanswcd.org/tree-shrub-program (January)
- Delaware Highlands Conservancy: delawarehighlands.org/events
- Garden clubs: Warwick Valley Gardeners (warwickgardeners.com), Community Garden Club of Liberty, Orange County clubs via CCE Orange
- Markets: pickocny.com and orangetourism.org (farms-and-markets, winter-farm-markets), sullivancatskills.com/series/callicoon-farmers-market, welcometonarrowsburg.com/events, Newburgh Common Ground market, Bethel Woods (bethelwoodscenter.org/peace-love-lights: holiday market, pop-ups, sing-alongs), Dogwood Acres and Pierson's Farm (Middletown), Museum Village (museumvillage.org/events)
- Maple: mapleweekend.com (March), Winterton Farms (Bloomingburg), Finding Home Farms (Middletown)
- Out of range: Stony Kill, Wild Ones Mid-Hudson, Hudson Valley Seed Co. New Paltz winter markets: no current source found on Oct 26.

### Lane 4: Walks, hikes, nature, races
- Races and charity walks: runsignup.com (search 12790, 50 miles, "walk" filter; search needs a browser, but single race pages open with WebFetch), act.alz.org, orangerunnersclub.org, Pine Bush, Matamoras, Milford, New Paltz, Livingston Manor turkey trots
- Mohonk Preserve: Wednesday walks mpreserve.ticketapp.org/portal/product/25/events, weekend hikes /product/26/events, 845-255-0919
- Minnewaska and Sam's Point: parks.ny.gov/visit/events (search "Minnewaska"), 845-255-0752; NY State Parks First Day Hikes parks.ny.gov/events/first-day-hikes (mid-December)
- Delaware Highlands Conservancy (walks, owl prowl, eagle watch training and bus tours)
- Pike County Conservation District "Hikes in Pike": pikeconservation.org/events
- Places: Mamakating / Sullivan O&W Rail Trail (sullivanoandw.com/trails/mamakating), Orange Heritage Trail (orangecountyny.gov/1475/Heritage-Trail), Mongaup Valley eagle blinds (dec.ny.gov), Basha Kill Area Association (thebashakill.org, 845-789-2846), MEEC (friendsofmeec.org)
- Also: Mid-Hudson Astronomical Association, Catskill Center (far), Black Rock Forest, Hudson Highlands Nature Museum, Orange County Walking Club, Sullivan 180
- Do NOT use friendsofsterlingforest.org (now a spam site) or wvlt.org (for-sale domain).

### Lane 5: Arts, culture, community, classes, town programs
- Town and village calendars: mamakating.gov Calendar (CID=14; MEEC events are here), Mamakating Parks and Rec, Village of Wurtsboro (wurtsboro.org), Town of Thompson (thompsonny.gov/events), Rosendale Recreation (townofrosendaleny.gov/recreation), Village of Montgomery, Ellenville, Liberty, Walden
- Arts: Wurtsboro Art Alliance, Catskill Art Space (catskillartspace.org/events and /classes), Wallkill River Center, Delaware Valley Arts Alliance (delawarevalleyartsalliance.org; far), Bethel Woods (bethelwoodscenter.org/programs/adults), Hurleyville Performing Arts Centre (hpacny.org), Shadowland Stages (Ellenville), Rosendale Theatre (rosendaletheatre.org WITHOUT www; the www address goes to another theater), Callicoon Theater (far), SUNY Orange Cultural Affairs, Unison
- Museums: Museum Village (Monroe), Sullivan County Historical Society (Hurleyville), Minisink Valley Historical Society
- County calendar: sullivancatskills.com/sullivan-catskills-event-calendar (month views; read the whole month)
- Holiday: tree lightings, parades, "Joy to Wurtsboro", Christmas markets (post mid-November)

### Lane 6: Social groups, volunteering, fitness
- Social: Meetup (search Wurtsboro, Middletown, Goshen; e.g. Women of Orange County and Beyond, Experience Hudson Valley), Two Farms Brewing trivia (twofarmsbrewing.com/events), Wurtsboro Fire Dept Ladies Auxiliary (wurtsborofd.com, 3rd Wed 6pm), Friends of Mamakating Library, Sullivan County Community Chorus, Sullivan Club 180
- Volunteering: Sullivan County SPCA (sullivanspca.org, Rock Hill), Pets Alive (petsalive.org), Catskill Animal Rescue, Goshen and Warwick humane societies, Regional Food Bank (regionalfoodbank.net/volunteer), Orange County RSVP (845-615-3728; name has "Senior"), Garnet Health auxiliary and volunteers, Habitat ReStore Newburgh, Hospice of Orange and Sullivan, Friends of the Port Jervis Library, Basha Kill Nature Watch, Mohonk Preserve and Delaware Highlands volunteers, Sullivan 180, local food pantries (Sullivan County food pantry guide PDF on sullivanny.gov)
- Fitness: YMCA of Middletown (middletownymca.org/join/schedules: group exercise, pool and gym PDFs; fetch tools are blocked, a browser works), Catskill Art Space yoga, Thompson pickleball, HPAC line dancing, Port Jervis community yoga (pjschools.org), Kim Lowe (kimlowe.fitness, Bloomingburg), Hidden Charm (hidden-charm-performance-training.com), Body Physics / Sgt. Cyndi (sgtcyndi.com)
- Not yet searched well (the Oct 26 search budget ran out): Rotary, Lions, Elks, Grange, church women's groups, Soroptimist, AAUW, newcomers clubs, choirs and community bands. Search these.

### Never reachable by the tools (do not count as checked)
Facebook and Instagram, middletownymca.org through WebFetch (use a browser), ulstertourism.com, bashakill.org, sullivanny.us parks, walkway.org, wallkillvalleylandtrust.org, scchorus.org, hospiceos.org, tuveemoralpacas.com, townofmamakating.com.

## Rules
- Change data only. Do not redesign the layout or remove sections or tabs. Do not change the Recently added / Interested / Not for me code.
- Keep variety. Mom's likes are a reason to look harder in those topics, never a reason to drop other kinds of things. Every week add some things outside her usual crafts (moving, nature, music, volunteering, social), so she keeps trying something different.
- The PDF must stay between 50 and 95 pages (it is 79 after the Oct 26 update). If a new item pushes it over, trim the least useful older entries.
- Never put personal secrets or passwords anywhere. Do not add "senior" branding.
- To undo a bad update: `git revert` the last commit and push.
