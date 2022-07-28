#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from scipy.stats import mannwhitneyu

def simple_heuristics(test_sample, control_sample):
    return test_sample.mean() > control_sample.mean()

def make_mw_heuristics(pvalue=0.05):
    def mw_heuristics(test_sample, control_sample):
        return mannwhitneyu(test_sample, control_sample, alternative='greater').pvalue < pvalue
    return mw_heuristics