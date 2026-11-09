/* Tobbe's Super Plugin - Hjaelp!-fanen.
 *
 * This file is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 */

#include "help_section.h"

#include "fonts.h"
#include "skin.h"
#include "help_content.h"

HelpSection::HelpSection() : SynthSection("help_section"), selected_(1) { }

Rectangle<int> HelpSection::getListBounds() {
  int padding = 12 * size_ratio_;
  int list_width = getWidth() * 0.32f;
  return Rectangle<int>(padding, padding, list_width, getHeight() - 2 * padding);
}

int HelpSection::getRowHeight() {
  int wanted = 30 * size_ratio_;
  int fits = getListBounds().getHeight() / tobbe_help::kNumTopics;
  return std::max(1, std::min(wanted, fits));
}

void HelpSection::paintBackground(Graphics& g) {
  paintBody(g);

  Colour primary = findColour(Skin::kWidgetPrimary1, true);
  Colour body_text = findColour(Skin::kBodyText, true);
  Colour bright_text = findColour(Skin::kTextComponentText, true);

  int padding = 12 * size_ratio_;
  Rectangle<int> list = getListBounds();
  int row_height = getRowHeight();

  Font row_font = Fonts::instance()->proportional_regular().withPointHeight(13.0f * size_ratio_);
  Font group_font = Fonts::instance()->proportional_title_regular().withPointHeight(10.0f * size_ratio_);

  g.setColour(findColour(Skin::kWidgetBackground, true).withAlpha(0.75f));
  g.fillRoundedRectangle(list.toFloat(), 6.0f * size_ratio_);

  for (int i = 0; i < tobbe_help::kNumTopics; ++i) {
    Rectangle<int> row(list.getX(), list.getY() + i * row_height, list.getWidth(), row_height);
    String title = String::fromUTF8(tobbe_help::kTopics[i].title);

    if (tobbe_help::kTopics[i].body == nullptr) {
      g.setColour(primary);
      g.setFont(group_font);
      g.drawText(title, row.reduced(padding, row_height / 6), Justification::bottomLeft, true);
      continue;
    }

    if (i == selected_) {
      g.setColour(primary.withAlpha(0.3f));
      g.fillRoundedRectangle(row.reduced(4, 1).toFloat(), 4.0f * size_ratio_);
    }

    g.setColour(i == selected_ ? bright_text : body_text);
    g.setFont(row_font);
    g.drawText(title, row.reduced(padding + padding / 2, 0), Justification::centredLeft, true);
  }

  if (selected_ < 0 || selected_ >= tobbe_help::kNumTopics || tobbe_help::kTopics[selected_].body == nullptr)
    return;

  Rectangle<int> text_area(list.getRight() + 2 * padding, padding,
                           getWidth() - list.getRight() - 3 * padding, getHeight() - 2 * padding);
  if (text_area.getWidth() <= 0 || text_area.getHeight() <= 0)
    return;

  int title_height = 34 * size_ratio_;
  g.setColour(primary);
  g.setFont(Fonts::instance()->proportional_title_regular().withPointHeight(20.0f * size_ratio_));
  g.drawText(String::fromUTF8(tobbe_help::kTopics[selected_].title),
             text_area.removeFromTop(title_height), Justification::centredLeft, true);
  text_area.removeFromTop(padding / 2);

  AttributedString text;
  text.append(String::fromUTF8(tobbe_help::kTopics[selected_].body),
              Fonts::instance()->proportional_regular().withPointHeight(13.5f * size_ratio_), body_text);
  text.setWordWrap(AttributedString::byWord);
  text.setLineSpacing(4.0f * size_ratio_);

  TextLayout layout;
  layout.createLayout(text, (float)text_area.getWidth());
  layout.draw(g, text_area.toFloat());
}

void HelpSection::mouseDown(const MouseEvent& e) {
  Rectangle<int> list = getListBounds();
  if (!list.contains(e.getPosition()))
    return;

  int index = (e.y - list.getY()) / getRowHeight();
  if (index < 0 || index >= tobbe_help::kNumTopics || index == selected_)
    return;
  if (tobbe_help::kTopics[index].body == nullptr)
    return;

  selected_ = index;
  repaintBackground();
}
