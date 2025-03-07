import re; # Importing regex module for text processing

# Text preprocessing before NLP processing
# This class removes unnecessary whitespaces and adds them where grammatically correct.
class FormatTextHandler:

    def format_whitespaces(unformated):
        """
        Formats whitespaces in the text:
        - Adds a space after periods (.) and commas (,), if missing.
        - Removes unnecessary leading and trailing spaces.
        - Removes extra spaces within the text.
        - Ensures no space exists before a period or a comma.
        """
        unformated = unformated.replace(".", ". ");
        unformated = unformated.replace(",", ", ");

        stripped_text = unformated.strip();

        stripped_text = " ".join(stripped_text.split());

        stripped_text = stripped_text.replace(" .", ".");
        cleaned = stripped_text.replace(" ,", ",");

        return cleaned;


    def change_wrong_words(text_with_ww):
        """
        Corrects words that were incorrectly processed by OCR.
        Also, removes hyphenated words at the end of lines.
        """

        text_with_ww = text_with_ww.replace(" go", " gđo");
        text_with_ww = text_with_ww.replace("pomladi", "pomladio");
        text_with_ww = text_with_ww.replace("55", "u");

        cleaned_text = re.sub(r"(\w+)-\s(\w+)", r"\1\2", text_with_ww);

        return cleaned_text;


    def throwOutNotWords(text):
        """
        Removes common patterns like citations in brackets (e.g., [2]).
        """

        not_a_word_pattern = r"\[\d+\s*\]";
        formatted_text = re.sub(not_a_word_pattern, "", text);

        return formatted_text;

# Logic for text preprocessing before NLP analysis
def cleaned_text_getter():
    """
    Reads a text file, applies formatting and correction functions, 
    and returns the cleaned text.
    """

    file = open('388.txt', encoding="utf8");
    unformatted_text = file.read();
    file.close();

    unformatted_text = FormatTextHandler.format_whitespaces(unformatted_text);
    unformatted_text = FormatTextHandler.change_wrong_words(unformatted_text);
    cleaned_text = FormatTextHandler.throwOutNotWords(unformatted_text);

    return cleaned_text;