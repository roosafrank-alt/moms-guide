# Monday update runbook (for the scheduled task)

Goal: keep Mom's Guide current. Mom lives in Wurtsboro NY 12790. She crochets and knits, gardens and walks, wants to meet friends and build a weekly routine, and dislikes anything branded "senior". Keep everything within about 45 minutes' drive. Write in plain, short words.

Live site: https://roosafrank-alt.github.io/moms-guide/ (GitHub Pages, branch main). A printed binder (56 pages) was made on Oct 20, 2026, so the user can reprint single pages.

## Files
- `source/packet.html` is the master. Everything is data inside one JS file: `DAYS` (Mon to Sun items made with `I(...)`), `REC` (recurrence pill per item, matched BY POSITION to the items in each weekday, so if you add or remove a day item you must add or remove the matching entry in `REC[day]`), events with `EV(date, name, time, where, drive, cost, phone, last, note)`, fitness `F(...)`, volunteering `V(...)`, `TABS`, and the tables.
- `source/ideas_data.py` holds the Ideas and Walks tabs (ARTS, GARD, HIKE, GROUP, RACES). `build_ideas.py` regenerates those tabs inside packet.html. Never edit the block between `// IDEAS BEGIN` and `// IDEAS END` in packet.html by hand. Edit ideas_data.py instead.
- `UPDATES` (near the bottom of packet.html, search "UPDATE LOG") feeds the "Recently updated" box on the phone home screen and the "Last updated" date everywhere.
- `source/build_site.py` builds index.html, the PDF and the service-worker cache. It runs the checks and stops with an error if anything is wrong.

## Each Monday
1. Set today's date from the system. Remove events whose last date has passed. Weekly items stay unless the source says they ended.
2. Check sources for NEW or CHANGED items (open the official page; never rely on memory):
   - Library calendars: Liberty (libertypubliclibrary.libcal.com), Mamakating (calendar.mamakatinglibrary.org), Crawford Monticello (ebcpl.libcal.com), Ellenville (eplm.org/calendar-2), Thrall, Pine Bush.
   - MEEC monthly events (pjschools.org community corner), Montgomery village calendar (villageofmontgomeryny.gov), Cornell Cooperative Extension Sullivan and Orange events, Rosendale Recreation, Delaware Highlands Conservancy, Wurtsboro Art Alliance, Catskill Art Space, Bethel Woods, farmers markets (pickocny.com, sullivancatskillsfarmersmarkets.com).
   - Walks and runs: runsignup.com, act.alz.org (Walk to End Alzheimer's), members.orangeny.com. Group walks and hikes in ideas_data.py.
   - SUNY Orange Encore: the spring 2027 catalog is expected in January. Recheck every Monday from mid-January.
   - Facebook and middletownymca.org block automated fetching. Do not rely on them.
2b. CHECK EVERY POSSIBLE SOURCE (the user's standing order). The list above is a starting point, not a limit. Also search the web broadly for the Wurtsboro area (about 45 minutes): town, village and county sites, Sullivan and Orange County tourism and event calendars, Ulster County, Mamakating, Bashakill, parks and trails, farms and markets, churches and community centers, schools, other libraries, galleries, studios and yarn shops, nature centers, Recreation.gov and ticketing sites, and any source used earlier in this guide. Search for crochet, knitting, fiber arts, gardening, walking and hiking groups, classes, free events and volunteering. Anything found still needs an official page before it is added (step 3).
3. Add only things you verified on an official page. Use badge `'c'` (dates confirmed) when the page shows the date, `'a'` (call first) when unsure. Put the source host in the existing link mapping (`LK`) only if it is missing. Never invent dates, prices, phone numbers or addresses. If you cannot verify, leave it out or mark it call first.
4. Open items to chase: Encore spring 2027, Dec to Mar events, Fiber Arts Saturday (time and place), Hidden Charm and Kim Lowe fitness locations, Fire Auxiliary meetings, Nov 1 Sky Stitching cost, a Liberty "Kindred Spirits" knitting circle (details missing), Port Jervis community yoga residency or library card question.
5. Add entries at the TOP of `UPDATES` in packet.html: `{ d: 'YYYY-MM-DD', t: 'short plain text', k: 'ev' }` where `k` is a tab key (`mon`..`sun`, `ev`, `walk`, `enc`, `fit`, `vol`, `ideas`, `me`, `host`, `plan`) or `'my'`. Only list real additions, changes and removals Mom would care about. If nothing changed, still change nothing and do not add an entry (the box keeps showing the last update).
6. Run `python3 source/build_site.py`. If it fails, fix the cause or revert your edits. Do not publish a broken build.
7. Commit all changes (index.html, sw.js, Moms_Activity_Packet.pdf, source/*) with a clear message and push to `main`.
8. Message the user a short summary: what was added, removed or changed, and what you could not verify. Keep it to a few lines.

## Rules
- Change data only. Do not redesign the layout or remove sections or tabs.
- Keep the PDF between 50 and 70 pages (it is 56 now). If a new item pushes it over, trim the least useful older entries.
- Never put personal secrets or passwords anywhere. Do not add "senior" branding.
- To undo a bad update: `git revert` the last commit and push.
