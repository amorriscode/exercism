pub fn reverse(input: &str) -> String {
    let mut answer = String::new();
    for letter in input.chars().rev() {
        answer.push(letter);
    }

    return answer;
}
