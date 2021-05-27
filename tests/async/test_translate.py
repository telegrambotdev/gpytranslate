"""
    gpytranslate - A Python3 library for translating text using Google Translate API.
    Copyright (C) 2020-2021  Davide Galilei

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import pytest

from typing import List, Dict, Any

from gpytranslate import Translator, TranslatedObject


@pytest.mark.asyncio
async def test_translate_auto():
    translator = Translator()
    translation: TranslatedObject = await translator.translate(
        "Ciao Mondo.", targetlang="en"
    )
    assert translation.text == "Hello World.", "Translations are not equal."


@pytest.mark.asyncio
async def test_translate_source():
    translator = Translator()
    translation: TranslatedObject = await translator.translate(
        "Ciao.", sourcelang="it", targetlang="en"
    )

    assert translation.text == "Hello.", "Translations are not equal."


@pytest.mark.asyncio
async def test_translate_list():
    translator = Translator()
    translations: List[TranslatedObject] = await translator.translate(
        ["Ciao Mondo.", "Come stai?"], targetlang="en"
    )

    assert [translation.text for translation in translations] == [
        "Hello World.",
        "How are you?",
    ], "Translations are not equal."


@pytest.mark.asyncio
async def test_translate_dict():
    translator = Translator()
    translations: Dict[Any, TranslatedObject] = await translator.translate(
        {1: "Ciao Mondo.", 2: "Come stai?"}, targetlang="en"
    )

    assert {k: v.text for k, v in translations.items()} == {
        1: "Hello World.",
        2: "How are you?",
    }, "Translations are not equal."
