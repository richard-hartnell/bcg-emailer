# you don't need to point to the meeting I guess

meeting_date = prompt('What is the date of the meeting?')

# write the reminder email for 1 week

week_reminder = '''
Hi all,

Here's the week-ahead reminder of our next Circus Guild meeting on ${date}.

Per usual, if you have any agenda items to add you can do so in the description field of the Google Calendar event. If you don't want a proposal subject to a ten-day waiting period presuming it passes this Sunday, then please submit it to the group in writing by this upcoming Thursday.

Also per usual, if you need to attend the event virtually just let us know.

RH
'''

# write the reminder email for 3 days

days_reminder = '''
Dear BCG,

Here is your additional reminder for the upcoming Guild meeting on ${meeting_date} at 5 PM.

If you intend to pass any proposals without a ten-day waiting period, please submit them to the Guild by writing by end of day today.
'''

# email to bcg

