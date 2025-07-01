export type ModelType = {
    id: number;
    hyper_params: {
        id: number;
        epochs: number;
        learning_rate: number;
    };
    test_train_split: {
        id: number;
        testing: number;
        training: number;
    };
    model_metrics: {
        id: number;
        accuracy: number;
        precision: number;
        f1_score: number;
        recall: number;
        confusion_matrix: string[][];
    };
};
