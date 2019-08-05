
from django import forms 

class ContactForm(forms.Form):


   NET_CHOCIE = '0'
   SERIES_CHOICE = '1'


   AUDIO_CHOICE = '0'
   VIDEO_CHOICE = '1'
   BOTH_CHOICE = '2'

   SERIES2_CHOICE = '0'
   CATEGORY_CHOICE = '1'

   BIG_RAP = '0'
   NEB_STOR = '1'
   STATE = '2'
   BOOKS = '3'
   FRIDAY = '4'
   PLAIN = '5'

   NEWS = '0'
   ARTS  = '1'
   SCIENCE = '2'
   SPORTS = '3'
   NEWS_AFFARIS = '4'
   ARTS_CULTURE = '5'
   COURT = '6'
   HISTORY = '7'
   LEGISLATURE = '8'
   NATURE = '9'
   OFFICE = '10'
   SCIENCE = '11'
   SPORTS = '12'
   STATE = '13'
   SUPREME = '14'

   
   AMS = '0'
   ANTIQUES = '1'
   AUSTIN = '2'
   FRONT = '3'
   GREAT_p = '4'
   INDEPENDENT = '5'
   NATURE = '6'
   NOV = '7'
   NEWS_HOUR = '8'
   POLDARK = '9'
   SHAKESPARE = '10'
   GREAT = '11'
   WOMEN = '12'
   OLD = '13'
   WASHINGTON = '14'

   THINGS = '15'
   ASK = '16'
   CAR = '17'
   FRESH = '18'
   MORNING = '19'
   BEING = '20'
   POINT = '21'
   RADIO_LAB = '22'
   SUNDAY = '23'
   TED = '24'
   MOTH = '25'
   SPLENDID = '26'
   AMERICAN_LIFE = '27'
   WAIT = '28'
   WEEKEND = '29'
   WEEKEND_SAT = '30'


   BEFORE = '0'
   AFTER = '1'
   Between = '2'




   FIRST_CHOICES = (
    ('-1', '----'),
    (NET_CHOCIE , 'net'),
    (SERIES_CHOICE , 'external')
     )

   CONTAIN_CHOICES = (
    ('-1', '----'),
    (AUDIO_CHOICE , 'audio'),
    (VIDEO_CHOICE , 'video'),
    (BOTH_CHOICE , 'all')
    )

   SERIES_CAT_CHOICE = (
    ('-1', '----'),
    (SERIES2_CHOICE , 'series'),
    (CATEGORY_CHOICE , 'category')

    )


   NET_SERIES = (
    ('-1', '----'),
    (BIG_RAP , 'Big Red Wrap-Up'),
    (NEB_STOR , 'Nebraska Stories'),
    (STATE ,'The State of Education in Nebraska'),
    (BOOKS, 'ALL About Books'),
    (FRIDAY , 'FRIDAY Live'),
    (PLAIN , 'The PlainStory')
    )

   NET_CATEGORIES = (
    ('-1', '----'),
    (NEWS , 'news'),
    (ARTS , 'arts'),
    (SCIENCE , 'science'),
    (SPORTS , 'sports'),
    (NEWS_AFFARIS , 'News & Public Affairs'),
    (ARTS_CULTURE , 'Arts & Culture'),
    (COURT , 'Court of Appeals'),
    (HISTORY , 'History'),
    (LEGISLATURE , 'Legislature'),
    (NATURE , 'Nature & Environment'),
    (OFFICE , 'Office of the Governor'),
    (SCIENCE , 'Science & Health'),
    (SPORTS , 'Sports'),
    (STATE , 'State Board of Education'),
    (SUPREME , 'Supreme Court')
    )

   EXTERNAL_VIDEOS = (
    ('-1', '----'),
    (AMS , 'American Experience'),
    (ANTIQUES , 'Antiques Roadshow'),
    (AUSTIN , 'Austin City Limits'),
    (FRONT , 'FRONTLINE'),
    (GREAT_p , 'Great Performances'),
    (INDEPENDENT , 'Independent Lens'),
    (NATURE , 'Nature'),
    (NOV , 'NOVA'),
    (NEWS_HOUR , 'NewsHour'),
    (POLDARK , 'Poldark'),
    (SHAKESPARE , 'Shakespeare'),
    (GREAT , 'The Great British Baking Show'),
    (WOMEN , 'The Woman in White'),
    (OLD , 'This Old House'),
    (WASHINGTON , 'Washington Week')
    )
    
   DATE_CHOICES = (
    ('-1', '----'),
    (BEFORE , 'before'),
    (AFTER , 'after'),
    (Between , 'between')
    )


    
   EXTERNAL_AUDIOS = (
    ('-1', '----'),
    (THINGS , 'All Things Considered'),
    (ASK , 'Ask Me Another'),
    (CAR , 'Car Talk'),
    (FRESH , 'Fresh Air'),
    (MORNING , 'Morning Edition'),
    (BEING , 'On being with Krista Tipper'),
    ( POINT, 'ON Point'),
    (RADIO_LAB , 'Radiolab Weekly'),
    (SUNDAY , 'Sunday Puzzle'),
    (TED , 'TED Radio Hour'),
    (MOTH , 'The Moth Radio Hour'),
    (SPLENDID , 'The Splendid Table'),
    (AMERICAN_LIFE , 'This American Life'),
    (WAIT , 'Wait Wait...Don’t Tell Me!'),
    (WEEKEND , 'Weekend Edition Saturday'),
    (WEEKEND_SAT , 'Weekend Edition Sunday')
    )


   BOTH = (
    ('-1', '----'),
    (THINGS , 'All Things Considered'),
    (ASK , 'Ask Me Another'),
    (CAR , 'Car Talk'),
    (FRESH , 'Fresh Air'),
    (MORNING , 'Morning Edition'),
    (BEING , 'On being with Krista Tipper'),
    ( POINT, 'ON Point'),
    (RADIO_LAB , 'Radiolab Weekly'),
    (SUNDAY , 'Sunday Puzzle'),
    (TED , 'TED Radio Hour'),
    (MOTH , 'The Moth Radio Hour'),
    (SPLENDID , 'The Splendid Table'),
    (AMERICAN_LIFE , 'This American Life'),
    (WAIT , 'Wait Wait...Don’t Tell Me!'),
    (WEEKEND , 'Weekend Edition Saturday'),
    (WEEKEND_SAT , 'Weekend Edition Sunday'),
    (AMS , 'American Experience'),
    (ANTIQUES , 'Antiques Roadshow'),
    (AUSTIN , 'Austin City Limits'),
    (FRONT , 'FRONTLINE'),
    (GREAT_p, 'Great Performances'),
    (INDEPENDENT , 'Independent Lens'),
    (NATURE , 'Nature'),
    (NOV , 'NOVA'),
    (NEWS_HOUR , 'NewsHour'),
    (POLDARK , 'Poldark'),
    (SHAKESPARE , 'Shakespeare'),
    (GREAT , 'The Great British Baking Show'),
    (WOMEN , 'The Woman in White'),
    (OLD , 'This Old House'),
    (WASHINGTON , 'Washington Week')
  )
  

   mediaSource = forms.ChoiceField(choices=FIRST_CHOICES , required = True , label='Your name')

   contain = forms.ChoiceField(choices=CONTAIN_CHOICES , required=False)

   category = forms.ChoiceField(choices=SERIES_CAT_CHOICE , required=False)

   netSeries = forms.ChoiceField(choices=NET_SERIES , required=False )


   netCategories = forms.ChoiceField(choices=NET_CATEGORIES , required=False)

   externalVideoSeries = forms.ChoiceField(choices=EXTERNAL_VIDEOS , required=False)

   externalAudioSeries = forms.ChoiceField(choices = EXTERNAL_AUDIOS , required=False)
   both = forms.ChoiceField(choices = BOTH , required=False)


   date = forms.ChoiceField(choices=DATE_CHOICES , required=False)

   number = forms.IntegerField(required = False , initial=50 )

   before = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }),
        required=False
    )



   after = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker2'
        }),
        required=False
    )






   





  



   




    
    
        
    


