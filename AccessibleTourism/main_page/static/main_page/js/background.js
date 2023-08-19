function createBackground() {

    const words = ['the', 'and', 'have', 'that', 'for', 'you', 'with', 'say', 'this', 'they', 'but', 'his', 'from', 'not',
             'she', 'what', 'their', 'can', 'who', 'get', 'would', 'her', 'all', 'make', 'about', 'know', 'will', 'one',
             'time', 'there', 'year', 'think', 'when', 'which', 'them', 'some', 'people', 'take', 'out', 'into', 'just',
             'see', 'him', 'your', 'come', 'could', 'now', 'than', 'like', 'other', 'how', 'then', 'its', 'our', 'two',
             'more', 'these', 'want', 'way', 'look', 'first', 'also', 'new', 'because', 'day', 'use', 'man', 'find',
             'here', 'thing', 'give', 'many', 'well', 'only', 'those', 'tell', 'very', 'even', 'back', 'any', 'good',
             'woman', 'through', 'life', 'child', 'work', 'down', 'may', 'after', 'should', 'call', 'world', 'over',
             'school', 'still', 'try', 'last', 'ask', 'need', 'too', 'feel', 'three', 'state', 'never', 'become',
             'between', 'high', 'really', 'something', 'most', 'another', 'much', 'family', 'own', 'leave', 'put',
             'old', 'while', 'mean', 'keep', 'student', 'why', 'let', 'great', 'same', 'big', 'group', 'begin', 'seem',
             'country', 'help', 'talk', 'where', 'turn', 'problem', 'every', 'start', 'hand', 'might', 'American',
             'show', 'part', 'against', 'place', 'such', 'again', 'few', 'case', 'week', 'company', 'system', 'each',
             'right', 'program', 'hear', 'question', 'during', 'play', 'government', 'run', 'small', 'number', 'off',
             'always', 'move', 'night', 'live', 'point', 'believe', 'hold', 'today', 'bring', 'happen', 'next',
             'without', 'before', 'large', 'million', 'must', 'home', 'under', 'water', 'room', 'write', 'mother',
             'area', 'national', 'money', 'story', 'young', 'fact', 'month', 'different', 'lot', 'study', 'book', 'eye',
             'job', 'word', 'though', 'business', 'issue', 'side', 'kind', 'four', 'head', 'far', 'black', 'long',
             'both', 'little', 'house', 'yes', 'since', 'provide', 'service', 'around', 'friend', 'important', 'father',
             'sit', 'away', 'until', 'power', 'hour', 'game', 'often', 'yet', 'line', 'political', 'end', 'among',
             'ever', 'stand', 'bad', 'lose', 'however', 'member', 'pay', 'law', 'meet', 'car', 'city', 'almost',
             'include', 'continue', 'set', 'later', 'community', 'name', 'five', 'once', 'white', 'least', 'president',
             'learn', 'real', 'change', 'team', 'minute', 'best', 'several', 'idea', 'kid', 'body', 'information',
             'nothing', 'ago', 'lead', 'social', 'understand', 'whether', 'watch', 'together', 'follow', 'parent',
             'stop', 'face', 'anything', 'create', 'public', 'already', 'speak', 'others', 'read', 'level', 'allow',
             'add', 'office', 'spend', 'door', 'health', 'person', 'art', 'sure', 'war', 'history', 'party', 'within',
             'grow', 'result', 'open', 'morning', 'walk', 'reason', 'low', 'win', 'research', 'girl', 'guy', 'early',
             'food', 'moment', 'himself', 'air', 'teacher', 'force', 'offer', 'enough', 'education', 'across',
             'although', 'remember', 'foot', 'second', 'boy', 'maybe', 'toward', 'able', 'age', 'policy', 'everything',
             'love', 'process', 'music', 'including', 'consider', 'appear', 'actually', 'buy', 'probably', 'human',
             'wait', 'serve', 'market', 'die', 'send', 'expect', 'sense', 'build', 'stay', 'fall', 'nation', 'plan',
             'cut', 'college', 'interest', 'death', 'course', 'someone', 'experience', 'behind', 'reach', 'local',
             'kill', 'six', 'remain', 'effect', 'yeah', 'suggest', 'class', 'control', 'raise', 'care', 'perhaps',
             'late', 'hard', 'field', 'else', 'pass', 'former', 'sell', 'major', 'sometimes', 'require', 'along',
             'development', 'themselves', 'report', 'role', 'better', 'economic', 'effort', 'decide', 'rate', 'strong',
             'possible']


    background_el = $('div[class=background]')[0]
    let require_len_num = Math.ceil(screen.height / 3 / 16);
    for (let lineNumber = 0; lineNumber < require_len_num; lineNumber++) {
        line = document.createElement("div");
        line.className = "background-line";
        line.style = "--d:" + Math.floor(Math.random() * 26) + "s";
        let lineLen = 0;
        while (lineLen < Math.ceil(screen.width / 8)) {
            let rnd = Math.floor(Math.random() * 6);
            let word = words[Math.floor(Math.random() * words.length)];
            lineLen += word.length;
            if (rnd === 0) {
                // add letter as it was typed wrong
                let letter = String.fromCharCode(97 + Math.floor(Math.random() * 26));
                let rndSplit = Math.floor(Math.random() * (word.length - 1)) + 1;

                line.appendChild(document.createTextNode(word.substring(0, rndSplit)));

                span_el = document.createElement("span");
                span_el.className = "strikethrough lower-case";
                span_el.innerText = letter;
                line.appendChild(span_el);

                line.appendChild(document.createTextNode(word.substring(rndSplit) + " "));

            } else if (rnd === 1) {
                // mark letter as it was missed
                let rndSplit = Math.floor(Math.random() * (word.length - 1)) + 1;

                line.appendChild(document.createTextNode(word.substring(0, rndSplit)));

                span_el = document.createElement("span");
                span_el.className = "added";
                span_el.innerText = word.substring(rndSplit, rndSplit + 1)
                line.appendChild(span_el);

                line.appendChild(document.createTextNode(word.substring(rndSplit + 1) + " "));
            } else {
                line.appendChild(document.createTextNode(word + " "));
            }
        }
        background_el.appendChild(line);
    }
}