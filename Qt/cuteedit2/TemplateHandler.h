#pragma once

// Qt
#include <QObject>

// Forward refs.
class QListView;
class QTextEdit;
class QModelIndex;
class QStringListModel;


class TemplateHandler : public QObject {
	Q_OBJECT
	public:
		TemplateHandler(QListView* view, QTextEdit* textEdit, QObject* parent);

	protected slots:
		void insertText(const QModelIndex& index);

	private:
		QTextEdit* mTextEdit;
		QStringListModel* mModel;
};

