export default function ConfusionMatrix({ matrix, labels }: { matrix: string[][], labels: string[] }) {
    const size = matrix.length;

    return (
        <div className="overflow-x-auto">
            <table className="table-auto border-collapse border border-gray-400">
                <thead>
                    <tr>
                        <th className="border border-gray-400 p-2"></th>
                        {labels
                            ? labels.map((label, i) => (
                                <th key={i} className="border border-gray-400 p-2">
                                    Pred: {label}
                                </th>
                            ))
                            : matrix[0].map((_, i) => (
                                <th key={i} className="border border-gray-400 p-2">
                                    Pred: {i}
                                </th>
                            ))}
                    </tr>
                </thead>
                <tbody>
                    {matrix.map((row, rowIndex) => (
                        <tr key={rowIndex}>
                            <th className="border border-gray-400 p-2">
                                {labels ? `Actual: ${labels[rowIndex]}` : `Actual: ${rowIndex}`}
                            </th>
                            {row.map((cell, colIndex) => (
                                <td key={colIndex} className="border border-gray-400 p-2 text-center">
                                    {cell}
                                </td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};
