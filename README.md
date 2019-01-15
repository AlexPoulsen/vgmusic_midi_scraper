# vgmusic_midi_scraper
Scrapes vgmusic.com for midi files. Written in Python 3.

It can probably scrape other sites for midi files too. Requires a list of links, where each link is a page containing containing links to midi files.

It assumes the files are in the same directory and are relative links (file.mid vs https://suchsitemuch.wow/files/file.mid). It may be updated to test if they are relative and only append the name of the directory the html page is in to them, as well as for supporting links that go to a specific page as opposed to a directory.