/* Tobbe's Super Plugin - Hjaelp!-fanen.
 *
 * This file is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 */

#pragma once

#include "JuceHeader.h"
#include "synth_section.h"

// En enkel fane med oppskrifter: liste over lyder til venstre, forklaring til hoyre.
// Tekstene ligger i help_content.h (generert av tools/help_content.py).
class HelpSection : public SynthSection {
  public:
    HelpSection();

    void paintBackground(Graphics& g) override;
    void mouseDown(const MouseEvent& e) override;

  private:
    Rectangle<int> getListBounds();
    int getRowHeight();

    int selected_;

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR(HelpSection)
};
