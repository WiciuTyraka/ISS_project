module.exports.emptyPlot= `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`