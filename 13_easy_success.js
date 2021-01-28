const romanToInt = function(s) {
    let numerals = s.split("")
    let count = 0;
    
    numerals.forEach((numeral,i) => {
        if(numeral === "M") numerals[i] = 1000
        if(numeral === "D") numerals[i] = 500
        if(numeral === "C") numerals[i] = 100
        if(numeral === "L") numerals[i] = 50
        if(numeral === "X") numerals[i] = 10
        if(numeral === "V") numerals[i] = 5
        if(numeral === "I") numerals[i] = 1
    })

    for(let i = 0; i < numerals.length; i++) {
        let numeral = numerals[i]
        if(numerals[i + 1] > numerals[i]) continue;
        if(i === 0) {
            count += numeral;
            continue;
        }
        if(numerals[i-1] < numeral) {
            count += numeral - numerals[i - 1]
        } else {
            count += numeral;
        }

    }
    return count
};

console.log(romanToInt("MCMXCIV"))