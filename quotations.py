import numpy as np

quotations = [
  "The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.",
  "Don’t Let Yesterday Take Up Too Much Of Today.",
  "You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.",
  "It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.",
  "If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You."
  "People Who Are Crazy Enough To Think They Can Change The World, Are The Ones Who Do.",
  "Failure Will Never Overtake Me If My Determination To Succeed Is Strong Enough.",
  "Entrepreneurs Are Great At Dealing With Uncertainty And Also Very Good At Minimizing Risk. That’s The Classic Entrepreneur.",
  "We May Encounter Many Defeats But We Must Not Be Defeated.",
  "Knowing Is Not Enough; We Must Apply. Wishing Is Not Enough; We Must Do.",
  "Imagine Your Life Is Perfect In Every Respect; What Would It Look Like?",
  "We Generate Fears While We Sit. We Overcome Them By Action.",
  "Whether You Think You Can Or Think You Can’t, You’re Right.” – Quote By Henry Ford",
  "Security Is Mostly A Superstition. Life Is Either A Daring Adventure Or Nothing.",
  "The Man Who Has Confidence In Himself Gains The Confidence Of Others.",
  "The Only Limit To Our Realization Of Tomorrow Will Be Our Doubts Of Today.",
  "Creativity Is Intelligence Having Fun.",
  "What You Lack In Talent Can Be Made Up With Desire, Hustle And Giving 110% All The Time.",
  "Do What You Can With All You Have, Wherever You Are.",
  "Develop An ‘Attitude Of Gratitude’. Say Thank You To Everyone You Meet For Everything They Do For You.",
  "You Are Never Too Old To Set Another Goal Or To Dream A New Dream.",
  "To See What Is Right And Not Do It Is A Lack Of Courage.",
  "Reading Is To The Mind, As Exercise Is To The Body.",
  "Fake It Until You Make It! Act As If You Had All The Confidence You Require Until It Becomes Your Reality.",
  "The Future Belongs To The Competent. Get Good, Get Better, Be The Best!",
  "For Every Reason It’s Not Possible, There Are Hundreds Of People Who Have Faced The Same Circumstances And Succeeded.",
  "Things Work Out Best For Those Who Make The Best Of How Things Work Out.",
  "A Room Without Books Is Like A Body Without A Soul.",
  "I Think Goals Should Never Be Easy, They Should Force You To Work, Even If They Are Uncomfortable At The Time.",
  "One Of The Lessons That I Grew Up With Was To Always Stay True To Yourself And Never Let What Somebody Else Says Distract You From Your Goals.",
  "Today’s Accomplishments Were Yesterday’s Impossibilities.",
  "The Only Way To Do Great Work Is To Love What You Do. If You Haven’t Found It Yet, Keep Looking. Don’t Settle.",
  "You Don’t Have To Be Great To Start, But You Have To Start To Be Great.",
  "A Clear Vision, Backed By Definite Plans, Gives You A Tremendous Feeling Of Confidence And Personal Power.",
  "There Are No Limits To What You Can Accomplish, Except The Limits You Place On Your Own Thinking.",
  "Integrity Is The Most Valuable And Respected Quality Of Leadership. Always Keep Your Word.",
  "Leadership Is The Ability To Get Extraordinary Achievement From Ordinary People",
  "Leaders Set High Standards. Refuse To Tolerate Mediocrity Or Poor Performance",
  "Clarity Is The Key To Effective Leadership. What Are Your Goals?",
  "The Best Leaders Have A High Consideration Factor. They Really Care About Their People"
]

def generateQuotation():
  number = np.random.randint(0, len(quotations))
  return quotations[number]